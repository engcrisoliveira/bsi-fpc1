entrada = input()
listaEntrada = entrada.split()

total = 0
totalInterno = 0

repeticoes = 0
dentroDoLoop = False

for elemento in listaEntrada:
    if elemento == "IO": #custo de 30
        if dentroDoLoop == True:
            totalInterno += 30
        else:
            total += 30
    elif elemento == "PROCSUM": #custo de 1
        if dentroDoLoop == True:
            totalInterno += 1
        else:
            total += 1
    elif elemento == "PROCMULT" or elemento == "MEM": #custo de 10
        if dentroDoLoop == True:
            totalInterno += 10
        else:
            total += 1
    elif elemento == "LOOP":
        dentroDoLoop = True
        totalInterno = 0
    elif elemento == "FIMLOOP":
        dentroDoLoop = False
        total += repeticoes * totalInterno
    elif elemento != "INICIO" and elemento != "FIM":
        repeticoes = int(elemento)
print(total)
