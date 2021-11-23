numeros = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito","nove", "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")

num = int(input("Insira um número de 0 a 20: "))
while True:
    if num < 0:
        num = int(input("Por favor, insira um numero válido de 0 a 20: "))
    elif num > 20:
        num = int(input("Por favor, insira um numero válido: "))
    else:
        break
print(numeros[num])