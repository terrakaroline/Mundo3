lista = []
listapar = []
listaimpar = []

while True:
    a = int(input("Insira um número: "))
    lista.append(a)
    if a % 2 == 0:
        listapar.append(a)
    elif a % 2 == 1:
        listaimpar.append(a)
    continuar = str(input("Deseja continuar? [S/N]"))
    if continuar in "Nn":
        break
print(lista)
print(listapar)
print(listaimpar)