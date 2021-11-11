from math import floor

#Entradas
lista = list(map(int, input().split()))
x = lista.pop(0)

def busca_binaria_recursiva(lista, x, comparacao=1):
    meio__da_lista = floor(len(lista)/2)
    if x == lista[meio__da_lista]:
        return comparacao
    elif x < lista[meio__da_lista]:
        if meio__da_lista == 0:
            return comparacao
        return busca_binaria_recursiva(lista[:meio__da_lista], x, comparacao + 1)
    else:
        if meio__da_lista +1 == len(lista):
            return comparacao
        return busca_binaria_recursiva(lista[meio__da_lista+1:],x, comparacao + 1)
resultado = busca_binaria_recursiva(lista,x)

#Saídas
print(resultado)