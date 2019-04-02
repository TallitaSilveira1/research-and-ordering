import itertools as it
import timeit

def bucketSort(alist):
    largest = max(alist)
    length = len(alist)
    size = largest/length
 
    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(alist[i]/size)
        if j != length:
            buckets[j].append(alist[i])
        else:
            buckets[length - 1].append(alist[i])
 
    for i in range(length):
        insertion_sort(buckets[i])
 
    result = []
    for i in range(length):
        result = result + buckets[i]
 
    return result
 
def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp

lista = list(it.permutations([1, 2, 3, 4, 5, 6], 6))
listaAux = []
listaPermut = []

for i in lista:
    listaAux.append(list(i))
    listaPermut.append(list(i))

tempos = []


for i in listaPermut:
    tempos.append(timeit.timeit('bucketSort({})'.format(i),setup="from __main__ import bucketSort",number=50))

maxIdx = tempos.index(max(tempos))
minIdx = tempos.index(min(tempos))

print('Pior caso: ', listaAux[maxIdx])
print('Melhor caso: ', listaAux[minIdx])
