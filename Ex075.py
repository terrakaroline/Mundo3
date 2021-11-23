x = input("Insira 4 números: ").split()
a,b,c,d = x
a = int(a)
b = int(b)
c = int(c)
d = int(d)

tup = (a,b,c,d)
print(tup)
c = 0
for position, i in enumerate(tup):
    if i == 9:
        c += 1
    if i == 3:
        print(f"O numero 3 aparece na posição {position}")
    if i % 2 == 0:
        print(f"{i} é um número par", end=" ")
        print(" ")

print(f"O numero 9 apareceu {c} vezes")
