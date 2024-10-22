from typing import List, Tuple, Union
from functools import reduce
import time
import random

# Nico Florez
# Jiacheng Tan


def generar_array_aleatorio(largo):
    return [random.randint(0, 20) for _ in range(largo)]

def BubbleSort(arreglo):
    n = len(arreglo)

    for i in range(n-1):
        for j in range(n-1-i):
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]

IntListOrTuple = Union[List[int], Tuple[int]]

def QuickSort(lista: IntListOrTuple) -> IntListOrTuple:
    if len(lista) > 1:
        pivote = lista[0]
        def incluir_numero_si_es_menor(
            mi_lista: IntListOrTuple, numero: int
        ) -> IntListOrTuple:
            if numero < pivote:
                mi_lista.append(numero)
            return mi_lista

        lista_menores = reduce(incluir_numero_si_es_menor, lista, [])
        def incluir_numero_si_es_mayor(
            mi_lista: IntListOrTuple, numero: int
        ) -> IntListOrTuple:
            if numero > pivote:
                mi_lista.append(numero)
            return mi_lista

        lista_mayores = reduce(incluir_numero_si_es_mayor, lista, [])
        return (
            QuickSort(lista_menores)
            + [pivote]
            + QuickSort(lista_mayores)
        )
    return [lista[0]] if len(lista) == 1 else []

largo_arreglo = 5000
arreglo_usado = generar_array_aleatorio(largo_arreglo)

n = 0
while n != 10:
    start = time.time()
    BubbleSort(arreglo_usado)
    end = time.time()
    print(end - start)
    n += 1
