lista = []

for pos, i in range(0, 5):
    n = int(input("Insira um número: "))
    if pos == 0:
        lista.append(n)
    if i < pos[0]:
        