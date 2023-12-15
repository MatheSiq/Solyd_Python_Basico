frase = 'Oi, tudo bem?'
lista_nomes = ['Joao', 'matheus', 'guilherme', 'diego']
lista_nomes.append('Gerald')
lista_nomes.append('Fulano')#adiciona valor
lista_nomes.remove('Joao')#remove valor
#lista_nomes.clear()#limpa a lista
lista_nomes.insert(3, 'Cirilo')#adiciona um nome no lugar definido
lista_nomes[0] = 'Robertinha'#modifica o valor de uma posição
contador_robertinha = lista_nomes.count('Robertinha')

print(lista_nomes, contador_robertinha, len(frase))#len conta a quantidade de itens dentro da lista
#valores positivos a lista funciona da esquerda pra direita, valores negativos a lista vai da direita pra esquerda.

print(frase.lower())#transforma os valores em minusculo
frase_separada = frase.split(',')#transforma a frase em lista
print(frase_separada)