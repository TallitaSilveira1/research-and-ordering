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

def CountingSort(array):
    n = len(array)
    maxValue = max(array) + 1
    count = [0] * maxValue
    
    for i in array:
        count[i] += 1
    i = 0
    for j in range(maxValue):
        for k in range(count[j]):
            array[i] = j
            i += 1
    return array


x = [10000, 20000, 30000, 40000, 50000]
yMelhorCaso = []
yMedioCaso = []
yPiorCaso = []

for i in x:
    yMelhorCaso.append(timeit.timeit("CountingSort({})".format(geraListaOrdenada(i)),setup="from __main__ import CountingSort",number=1))
    
    lista = geraListaOrdenada(i)
    random.shuffle(geraListaOrdenada(i))
    yMedioCaso.append(timeit.timeit("CountingSort({})".format(lista), setup="from __main__ import CountingSort", number=1))

    yPiorCaso.append(timeit.timeit("CountingSort({})".format(geraListaInvertida(i)),setup="from __main__ import CountingSort",number=1))

casos = [yMelhorCaso, yMedioCaso, yPiorCaso]
casosLabel = ['Melhor caso', 'Medio caso', 'Pior caso']
desenhaGrafico(x, casos, casosLabel, 'CountingSortCasos.png')
