# Uma classe deve ter apenas uma responsabilidade, ou podemos definir isso pelo acrônimo SOLID
# S - Single responsibility principle
# O - Open/closed principle
# L - Liskov substitution principle
# I - Interface segregation principle
# D - Dependency inversion principle

# Os GETTERS e SETTERS só devem ser criados caso seja realmente preciso

class Conta:
    def __init__(self,numero,titular,saldo,limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def saldo(self,):
        print(f'O saldo da conta {self} é {self.__saldo}')

    def limite(self):
        print(f'O limite da conta {self} é {self.__limite}')

    def deposita(self,valor):
        int(valor)
        self.__saldo += valor


    def pode_sacar(self,valor_a_sacar):#Metodo só pode servir para facilitar outros metodos, e não deve ser chamado fora da classe
        valor_disponivel =self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel

    def saca(self,valor):
        if(self.pode_sacar()):
            self.__saldo -= valor
        else:
            print('O valor inserido ultrapassou o limite')

    def transfere(self,destino,valor):
        int(valor)
        str(destino)
        self.saca(valor)
        destino.deposita(valor)
        print(f'O valor {valor} foi transferido para a conta {destino}')
#Getters
    @property
    def saldo(self):
        return self.__saldo
    @property
    def limite(self):
        return self.__limite
    @property
    def titular(self):
        return self.__titular.title()
    @property
    def numero(self):
        return self.__numero

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_banco():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}
#Setters
    @saldo.setter
    def titular(self,titular):
        self.__titular = titular
    @limite.setter
    def limite(self,limite):
        self.__limite = limite

