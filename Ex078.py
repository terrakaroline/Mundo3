numeros = []
mai = 0
men = 0
for c in range (0, 5):
    numeros.append(int(input(f"Digite um valor para a posição {c}: ")))
    if c == 0:
        mai = men = numeros[c]
    else:
        if numeros[c] > mai:
            mai = numeros[c]
        if numeros[c] < men:
            men = numeros[c]

print("=-" * 30)
print(f"Você digitou os valores {numeros}")
print(f"O maior valor digitado foi {mai} nas posições", end=" ")
for i, v in enumerate(numeros):
    if v == mai:
        print(f"{i}", end=" e ")
print(f"o menor valor digitado foi {men} nas posições", end=" ")
for i, v in enumerate(numeros):
    if v == men:
        print(f"{i}", end=" ")
    
#e o menor foi {menor} na posição {numeros.index(menor)}")