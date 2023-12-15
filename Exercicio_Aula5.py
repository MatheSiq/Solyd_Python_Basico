quatidade_convidados = int(input('Quantos convidados estarão presentes na festa? '))

x = 1

nomes = []

while x <= quatidade_convidados:
    nomes.append(input("Escreva o nome do convidado " + str(x) + ': '))
    x += 1
print()
print()
print('A LISTA DE CONVIDADOS É: ')

for i in nomes:
    print(i)