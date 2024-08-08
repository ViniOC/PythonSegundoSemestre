import time

def buscaBinaria ( vet, x):
    inicio = 0
    fim = len(vet)-1
    while inicio <= fim:
        meio = (inicio +fim)//2
        if vet [meio]>x:
            fim = meio -1
        elif vet[meio] < x:
            inicio = meio +1
        else :
            return meio 
    return -1

def BuscaSimples ( vet, x):
    for i in range (len(vet)):
        if vet[i] == x:
            return i 
    return -1


tempo_inicio_binaria = time.time()
array = [0] * 10_000_000
print (buscaBinaria(array, 100_000 ))
tempo_final_binaria  = time.time()
print('Tempo de execução da busca binária: ', tempo_final_binaria - tempo_inicio_binaria)

tempo_inicio = time.time()
print(BuscaSimples(array, 100_000))
tempo_final = time.time()
print('Tempo de execução da busca simples: ', tempo_final - tempo_inicio)