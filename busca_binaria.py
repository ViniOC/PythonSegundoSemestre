import time

def busca_binaria(conjunto: list, valor:object) -> int:
    ini = 0
    fim = len(conjunto) - 1
    while ini <= fim:
        meio = (ini + fim) // 2
        if conjunto[meio] == valor:
            return meio
        elif conjunto[meio] < valor:
            ini = meio + 1
        else:
            fim = meio - 1
    