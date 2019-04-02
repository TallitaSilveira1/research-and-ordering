import random
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt

def desenhaGrafico(x, y, graphLabel, fileName, xl = "Quantidade de números", yl = "Tempo"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    for i in range(3):
        ax.plot(x, y[i], label = graphLabel[i])
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(fileName)

def geraListaInvertida(tam):
    lista = []
    while tam > 0:
        lista.append(tam)
        tam-=1
    return lista

def geraListaOrdenada(tam):
    lista = []
    for i in range(tam):
        lista.append(i)
    return lista

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


x = [10000, 20000, 30000, 40000, 50000]
yMelhorCaso = []
yMedioCaso = []
yPiorCaso = []

for i in x:
    yMelhorCaso.append(timeit.timeit("bucketSort({})".format(geraListaOrdenada(i)),setup="from __main__ import bucketSort",number=1))
    
    lista = geraListaOrdenada(i)
    random.shuffle(geraListaOrdenada(i))
    yMedioCaso.append(timeit.timeit("bucketSort({})".format(lista), setup="from __main__ import bucketSort", number=1))

    yPiorCaso.append(timeit.timeit("bucketSort({})".format(geraListaInvertida(i)),setup="from __main__ import bucketSort",number=1))

casos = [yMelhorCaso, yMedioCaso, yPiorCaso]
casosLabel = ['Melhor caso', 'Medio caso', 'Pior caso']
desenhaGrafico(x, casos, casosLabel, 'BucketSortCasos.png')
