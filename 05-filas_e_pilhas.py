#Entrada
lista = list(input())

pilha = list()

while len(lista) > 0:
    ultimo_elemento = lista.pop()
    if ultimo_elemento in ['}', ']', ')']:
        pilha.append(ultimo_elemento)
    elif ultimo_elemento in ['(', '[', '{']:
        if len(pilha) == 0:
            lista.append(ultimo_elemento)
            break
        if ultimo_elemento == '(':
            if pilha.pop() == ')':
                continue
            lista.append(ultimo_elemento)
            break
        elif ultimo_elemento == '[':
            if pilha.pop() == ']':
                continue
            lista.append(ultimo_elemento)
            break
        elif ultimo_elemento == '{':
            if pilha.pop() == '}':
                continue
            lista.append(ultimo_elemento)
            break
    else:
        continue

if len(lista) != 0 or len(pilha) != 0:
    print('casamento imperfeito')
else:
    print('casamento perfeito')

