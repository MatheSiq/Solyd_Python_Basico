#Tuplas, dicionários e conjuntos

minha_tupla = ('Matheus', 'Robertinha') #Igual lista, mas não é possível modificar a quantidade de objetos dentro, não é dinãmico.
meu_dicionario = {'nome': 'joão', 'idade' : 12} #hash table, possui uma chave e um valor
meu_conjunto = {'matheus', 'joao', 'ricardo'} #conjunto é dinâmico, e não possui itens repetidos, não possui ordem, 0,1,2,3...

# print(minha_tupla)
# print(meu_dicionario)
# print(meu_conjunto)

for i in meu_dicionario:
     print(i,':',meu_dicionario[i])
     # print(meu_dicionario[i]) #para puxar o valor de uma key, usando um .values eu puxo os valores
