from random import randint

a = randint(0,100)
b = randint(0,100)
c = randint(0,100)
d = randint(0,100)
e = randint(0,100)

aleatory = (a, b, c, d, e)
print(aleatory)
maior = 0
menor = 101
for i in aleatory:
    if i > maior:
        maior = i
    elif i < menor:
        menor = i

print(f"O maior número é {maior} e o menor é {menor}")