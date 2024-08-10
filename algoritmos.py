# Algoritmos
#   - Busca: simples e binária
#   - Ordenação: selection, insertion e bubble
# - Matrizes (lista de listas)
# * Checkpoint 4
 
# - Dicionário e Conjuntos (set)
# - Exceções
# - Arquivos: texto e json
# * Checkpoint 5
 
# - Banco de dados: Oracle
# - API
# * Checkpoint 6

def busca(conjunto: list, valor: float) -> int:
    i = 0
    while i < len(conjunto) and conjunto[i] != valor:
        i += 1
    if i == len(conjunto):
        return -1
    else:
        return i
    
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 10
resp = busca(lista, x)
print (resp)

lista = [0] * 100_000_000
resp = busca(lista, x)
print (resp)