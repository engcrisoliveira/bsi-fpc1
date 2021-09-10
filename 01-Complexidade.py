comandos = input()
lista_comandos = comandos.split()

custo_total = 0
custo_loop = 0

repeticoes_loop = 0
dentro_loop = False

custos ={"INICIO":0, "IO":30, "PROCSUM":1, "PROCMULT":10, "MEM":10, "FIM":0 }

for elemento in lista_comandos:
    if elemento == "LOOP":
        dentro_loop = True
        custo_loop = 0
    elif elemento == "FIMLOOP":
        dentro_loop = False
        custo_total += custo_loop * repeticoes_loop
    elif elemento.isnumeric():
        repeticoes_loop = int(elemento)
    else:
        if dentro_loop:
            custo_loop += custos[elemento]
        else:
            custo_total += custos[elemento]
print(custo_total)S
