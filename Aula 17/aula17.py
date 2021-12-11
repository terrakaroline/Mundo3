#listas em python

lanche = ["hamburguer", "suco", "pizza", "pudim"]
print(lanche)
lanche[3] = "picolé"
print(lanche)

#Diferente das tuplas, as listas podem ser modificadas

lanche.append("cookie") 
print(lanche)
#Use o append para adicionar um item ao fim da lista

lanche.insert(2,"cachorro-quente")
print(lanche)

#Use o insert para adicionar um item em uma posição específica da lista

del lanche[3]
print(lanche)
lanche.pop(2)
print(lanche)
#usado para excluir um item específico da lista, o .pop normalmente é utilizado para eliminar o último item, mas há a possibilidade de dar como parâmetro o item que vc quiser eliminar

lanche.remove("suco")
print(lanche)
#Com este comando, vc remove um item específico da lista

if "hamburguer" in lanche:
    lanche.remove("hamburguer")
    print(lanche)

#valores = list(range(4,11))
#print(valores)
#cria uma lista de valores indicados pelo range

valores = [8, 2, 5, 4, 9, 3, 0]
print(len(valores)) #mostra quantos valores tem uma lista
