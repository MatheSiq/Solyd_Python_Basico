from banco import Cliente
from banco import Conta

nome = input('Qual é o seu nome? ')
cpf = (input('Escreva seu CPF, apenas os numeros '))
verificacao = (len(cpf))
idade = int(input('Qual é a sua idade? '))
saldo = float(input('Qual é o saldo da sua conta bancaria? '))
limite = float(input('Qual é o seu limite negativo da sua conta bancaria? '))

Matheus = Cliente(nome,cpf,idade)
Inter = Conta(nome,saldo,limite)

while True:
    print()
    print('1- Sacar')
    print('2- Depositar')
    print('3- Verificar Saldo')
    print('4- Sair')
    print()
    escolha = int(input('Escolha uma opção(1,2,3,4): '))
    print()

    if escolha == 1:
        valor = int(input('Qual é o valor a ser retirado da conta? '))
        if valor > Inter.saldo:
            print()
            print('Não é possivel sacar esse valor')
            print()
        else:
            Inter.sacar(valor)
            print()
            print('Saldo=', Inter.saldo)
            print()

    elif escolha == 2:
        valor = int(input('Qual é o valor a ser adicionado da conta? '))
        Inter.depositar(valor)
        print()
        print('Saldo=', Inter.saldo)
        print()

    elif escolha == 3:
        print()
        print('O saldo da conta é', Inter.saldo)
        print()

    elif escolha == 4:
        break