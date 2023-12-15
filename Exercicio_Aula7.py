#Escreva uma função que recebe um objeto de coleção(lista, conjunto, tupla, dicionario)
# e retorna o valor do maior numero dessa coleção, e o menor


def listagem1(lista):
    a = max(lista)
    b = min(lista)
    return a, b

i = listagem1([1,67,6,84,75,8854,965,755,422,4])#na hora de inserir o valor do item da fução, é necessário declarar a lista com colchetes
print(i)