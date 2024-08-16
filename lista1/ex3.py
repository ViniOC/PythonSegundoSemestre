def tiraRepetidos (vet):
    vet2 = []
    for i in range (len(vet)):
        if vet[i] not in vet2:
            vet2.append(vet[i]) 
    return vet2

list = [1, 1, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9,10, 10]

print(list)
print (tiraRepetidos(list))