num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)
num.append(7) #adiciona um item no fim da lista
num.sort() #organiza os itens
print(num)
num.sort(reverse=True) #deixa os valores em ordem reversa
num.insert(2, 0) #Adiciona um item na posição indicada
num.pop() #remove o último valor, coloque um número nos parenteses para indicar
print(num)
num.remove(2) #remove um item que está dentro da lista

if 4 in num:
    num.remove(4)
else:
    print("Não achei o número 4")

print(num)
print(f"Essa lista tem {len(num)} elementos.")

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)

for c, i in enumerate(valores):
    print(f"Na posição {c} encontrei o valor {i}!")
print("Cheguei ao final da lista.")

v = list()
for cont in range (0, 5):
    v.append(int(input("Digite um valor: ")))
print(v)

for p, n in enumerate(v):
    print(f"Na posição {p} encontrei o valor {n}")

a = [2, 3, 4, 7]
b = a[:] #assim se pega uma cópia de a dentro de b
b[2] = 8
print(a)
print(b)