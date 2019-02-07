from random import randint
from timeit import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt

def listGenerator(lenList):
    generated = []
    for i in range(lenList):
        n = randint(1,1*lenList)
        if n not in generated: generated.append(n)
    return generated

def bubbleSort(listToSort):
    lenList = len(listToSort)
    swap = 0
    swapped = True
    while swapped:
        swapped = False
        for index in range(lenList):
            for i in range(0, lenList-index-1):
                if listToSort[i] > listToSort[i+1]:
                    listToSort[i], listToSort[i+1] = listToSort[i+1], listToSort[i]
                    swapped = True
                    swap += 1
    
    return swap

lenghts = [10000,20000,30000,40000,50000]

times = []
swaps = []

for lenght in lenghts:
    listSort = listGenerator(lenght)
    swaps.append(bubbleSort(listSort))

    times.append(timeit("bubbleSort({})".format(listSort),setup="from __main__ import bubbleSort",number=1))

print(swaps)

def drawGraph(x,y,name, yl = "Time", xl = "List lenght"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Ascending")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(name)
    plt.show()

drawGraph(lenghts,swaps,"graph_bubble_swaps.png","Swaps")
drawGraph(lenghts,times,"graph_bubble_time.png")