def organiza(lista: list, pos: int):
    # pos = len(lista) -1
    aux = lista [pos] 

    while lista [pos-1] > aux and pos > 0:
        lista [pos] = lista[pos -1]
        pos = pos -1
    
    lista [pos] = aux
    




def insertion_sort(lista: list):
    for i in range(1, len(lista)):
        organiza(lista, i)
    


# lista = [5, 7, 11, 14, 25, 13]
lista = [2, 6, 10, -1, 0, 4, 24, 17, 14, 15, 8, 6]
print(lista)
insertion_sort(lista)
print (lista)
