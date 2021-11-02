
#Entrada de dados
entrada = list(map(int, input().split(" ")))

quantidade_container = entrada.pop(0)
tamanho_container = entrada.pop(0)
quantidade_insercoes = entrada.pop(0)
elementos_para_inserir = entrada[:quantidade_insercoes]
elementos_para_buscar = entrada[quantidade_insercoes:]

#Loop dentro da lista
containers = [None for i in range(quantidade_container * tamanho_container)]

#Inserir valor na tabela hash
def inserir(valor):
    hash = valor % quantidade_container
    for i in range(tamanho_container):
        if containers[hash*tamanho_container+i] is None:
            containers[hash*tamanho_container+i] = valor
            break

while len(elementos_para_inserir) != 0:
    valor = elementos_para_inserir.pop(0)
    inserir(valor)

#Buscar na tabela hash
def buscar(elemento):
    comparacoes = 0
    hash = elemento % quantidade_container
    for i in range(tamanho_container):
        if elemento == containers[hash*tamanho_container+i] or containers[hash*tamanho_container+i] is None:
            comparacoes += 1
            return comparacoes
        else:
            comparacoes += 1
    return comparacoes

comparacoes = []

while len(elementos_para_buscar) != 0:
    elemento = elementos_para_buscar.pop(0)
    vezes = buscar(elemento)
    comparacoes.append(vezes)

comparacoes = map(str, comparacoes)
saida = " ".join(comparacoes)
print(saida)