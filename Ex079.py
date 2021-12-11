lista = []
nitens = int(input("Quantos valores deseja adicionar? "))

for i in range(0, nitens):
    n = int(input("Insira um número: "))
    if n not in lista:
        lista.append(n)
lista.sort()
print(lista)