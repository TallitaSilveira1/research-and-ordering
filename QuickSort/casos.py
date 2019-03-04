from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys
import itertools as it
from random import randrange
sys.setrecursionlimit(1000000)


def desenhaGrafico(x, y, graphLabel, fileName, xl = "Quantidade de números", yl = "Tempo"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    for i in range(3):
        print(y[i], graphLabel[i])
        ax.plot(x, y[i], label = graphLabel[i])
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(fileName)    

def geraLista(tam):
    lista = []
    while tam > len(lista):
        n = randint(1, 1*tam)
        if n not in lista: lista.append(n)
    return lista        
        
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


x = [10000, 20000, 30000, 40000, 50000]

yMelhorCaso = []
yMedioCaso = []
yPiorCaso = []

for i in x:
    yMelhorCaso.append(timeit.timeit("QuickSort({})".format(sorted(geraLista(i))),setup="from __main__ import QuickSort",number=1))
    
    yMedioCaso.append(timeit.timeit("QuickSort({})".format(geraLista(i)),setup="from __main__ import QuickSort",number=1))
    
    yPiorCaso.append(timeit.timeit("QuickSort({})".format(sorted(geraLista(i), reverse=True)),setup="from __main__ import QuickSort",number=1))
    
casos = [yMelhorCaso, yMedioCaso, yPiorCaso]
casosLabel = ['Pior caso', 'Medio caso', 'Melhor caso']
desenhaGrafico(x, casos, casosLabel, 'QuickSortCasos.png')
