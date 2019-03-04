import itertools as it
import timeit
from random import randrange

def partition(lst, start, end, pivot):
    lst[pivot], lst[end] = lst[end], lst[pivot]
    store_index = start
    for i in range(start, end):
        if lst[i] < lst[end]:
            lst[i], lst[store_index] = lst[store_index], lst[i]
            store_index += 1
    lst[store_index], lst[end] = lst[end], lst[store_index]
    return store_index


def quick_sort(lst, start, end):
    if start >= end:
        return lst
    pivot = randrange(start, end + 1)
    new_pivot = partition(lst, start, end, pivot)
    quick_sort(lst, start, new_pivot - 1)
    quick_sort(lst, new_pivot + 1, end)


def QuickSort(lst):
    quick_sort(lst, 0, len(lst) - 1)
    return lst


lista = list(it.permutations([1, 2, 3, 4, 5, 6], 6))

aux = []
listPermut = []

for i in lista:
    aux.append(list(i))
    listPermut.append(list(i))

times = []

for i in listPermut:
    times.append(timeit.timeit('QuickSort({})'.format(lista),setup="from __main__ import QuickSort",number=1))
    
maxIndex = times.index(max(times))
minIndex = times.index(min(times))

print('Pior caso: ', aux[maxIndex])
print('Melhor caso: ', aux[minIndex]) 
