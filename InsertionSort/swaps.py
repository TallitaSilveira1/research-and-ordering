import itertools as it

def insertionSort(arr):
    swaps = 0
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] :
                swaps+=1
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key
    return swaps

#Achando o pior caso usando permutacoes
    
#Lista com todas as permutacoes
lista = list(it.permutations([1, 2, 3, 4, 5, 6], 6))

#Convertendo as tuplas em listas
listaPermut = []
listaAuxPermut = []
for i in lista:
    listaPermut.append(list(i))
    listaAuxPermut.append(list(i))

#Lista para guardar o numero de swaps 
swaps = [] 

for i in range(len(listaPermut)):
    swaps.append(insertionSort(listaPermut[i]))

maxIndex = swaps.index(max(swaps))
minIndex = swaps.index(min(swaps))

print('Pior caso:', listaAuxPermut[maxIndex],  ', Swaps:', swaps[maxIndex])
print('Melhor caso:', listaAuxPermut[minIndex], ', Swaps:', swaps[minIndex])