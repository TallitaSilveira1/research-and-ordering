import random
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import itertools as it
mpl.use('Agg')

def geraListaAle(tam):
    lista = []
    for i in range(tam):
        lista.append(i)
    random.shuffle(lista)
    return lista

def geraListaCre(tam):
    lista = []
    for i in range(tam):
        lista.append(i)
    return lista

def geraListaDec(tam):
    lista = []
    n = tam
    for i in range(tam):
        lista.append(n)
        n -=1
    return lista

def shellSort (lista):
    tam = len(lista)
    h = tam/2
    while (h>0):
        h = int(h)
        i = h
        while (i<tam):
            aux = lista[i]
            j = i
            while (j >=h and aux < lista[j-h]):
                lista[j] = lista [j-h]
                j = j-h
            lista[j] = aux
            i += 1
        h = h/2


def desenhaGrafico(x, pc, mc, ae, name, xl = "Entradas", yl = "Tempo (s)"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, pc, label = "Pior Caso")
    ax.plot(x, mc, label="Melhor Caso")
    ax.plot(x, ae, label="Aleatório")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(name)

x = [10000, 20000, 30000, 40000, 50000]

PiorCaso = []
MelhorCaso = []
CasoAle = []


for i in x:
    lista = geraListaDec(i)
    PiorCaso.append(timeit.timeit('shellSort({})'.format(lista),setup="from __main__ import shellSort",number=1))
    
    lista = geraListaAle(i)
    CasoAle.append(timeit.timeit('shellSort({})'.format(lista),setup="from __main__ import shellSort",number=1))
    
    lista = geraListaCre(i)
    MelhorCaso.append(timeit.timeit('shellSort({})'.format(lista),setup="from __main__ import shellSort",number=1))

desenhaGrafico(x, PiorCaso, MelhorCaso, CasoAle, "graph_time.png")

lis = [1, 2, 3, 4, 5, 6]
permut = list(it.permutations(lis,6))
tempo = []

for i in permut:
    tempo.append(timeit.timeit('shellSort({})'.format(permut),setup="from __main__ import shellSort",number=1))

maior = tempo.index(max(tempo))
menor = tempo.index(min(tempo))

print('Tempo maior:',max(tempo))
print(permut[maior])
print("\n")
print('Tempo menor:',max(tempo))
print(permut[maior])
