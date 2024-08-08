def organizaArray (vetor):
    for i in range (1, len(vetor)):
        arrayOrganizado = vetor[i]
        
        j = i - 1
        while j >= 0 and arrayOrganizado < vetor[j]:
            vetor [j+1] = vetor [j]
            j -= 1
            vetor [j + 1 ] = arrayOrganizado


def verificaSeTemSoma (vetor, x):
    inicio = 0
    fim = len(vetor) -1
    soma = vetor[inicio] + vetor[fim]
    while inicio != fim:
        for i in range (len(vetor)):
            if (soma == x):
                return True
            elif (soma > x ):
                fim = fim - 1
                soma =vetor [inicio] + vetor[fim]
            elif(soma < x ):
                inicio = inicio + 1
                soma = vetor [inicio] + vetor [fim]
            else:
                return False

array = [2, 5,-7, 9, 3, 10, 15, 6]

print (array)

organizaArray(array)


print ("Array organizado", array)

print (verificaSeTemSoma(array, 11))

