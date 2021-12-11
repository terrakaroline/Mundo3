from random import randint

aleatory = (randint(0,100),randint(0,100),randint(0,100),randint(0,100),
randint(0,100))
print("Os valores sorteados foram: ")
for n in aleatory:
    print(f"{n} ", end="")
print(f"\nO maior número é {max(aleatory)} e o menor é {min(aleatory)}")