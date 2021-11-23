lanche = ("Hamburguer", "Suco", "Pizza","Pudim") #criação de uma tupla
for cont in range(0, len(lanche)): #contador usando range e len
    print(lanche[cont])

for cont in range(0, len(lanche)):
    print(f"Digite o número {cont} se quiser {lanche[cont]}") # se quiser contabilizar o numero do item
print(len(lanche))

for comida in lanche: #contador composto
    print(f"Eu vou comer {comida}")

for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")
print("Vou comer pra caramba!")

for comida in lanche:
    print(f"Eu vou comer {comida}")

print(sorted(lanche)) #mostra a tupla em ordem

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
print(c)
print(d)
print(len(c)) #Mostra quantos números possui a tupla
print(c.count(5)) #mostra quantas vezes um numero aparece na tupla
print(c.index(8)) #mostra a posição em que está um item na tupla
print(c.index(2, 4)) #mostra a posição do item a partir de uma determinada posição

pessoa = ("Gustavo", 39, "M", 99.88)
print(pessoa)
del(pessoa) #exclui a tupla inteira, mas não se pode deletar apenas um elemento da tupla