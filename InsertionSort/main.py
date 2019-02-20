from random import randint
import timeit
import itertools as it
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.use('Agg')

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

def insertionSort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 

def geraLista(tam):
    lista = []
    while tam > len(lista):
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

x = [10000, 20000, 30000, 40000, 50000]

yMelhorCaso = []
yPiorCaso = []
yMedioCaso = []

for i in x:
    lista = geraLista(i)
    yMelhorCaso.append(timeit.timeit("insertionSort({})".format(sorted(lista)),setup="from __main__ import insertionSort",number=1))

    yPiorCaso.append(timeit.timeit("insertionSort({})".format(sorted(lista, reverse=True)),setup="from __main__ import insertionSort",number=1))
    
    yMedioCaso.append(timeit.timeit("insertionSort({})".format(lista),setup="from __main__ import insertionSort",number=1))

casos = [yPiorCaso, yMedioCaso, yMelhorCaso]
casosLabel = ['Pior caso', 'Medio caso', 'Melhor caso']
desenhaGrafico(x, casos, casosLabel, 'CasosInsertionSort.png')
