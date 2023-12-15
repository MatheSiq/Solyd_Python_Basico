class Cliente:

    def __init__(self,nome,cpf,idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

class Conta:

    def __init__(self,cliente,saldo,limite_negativo):
        self.cliente = cliente
        self.saldo = saldo
        self.limite_negativo = limite_negativo

    def sacar(self,valor):
        self.saldo -= valor

    def depositar(self,valor):
        self.saldo += valor