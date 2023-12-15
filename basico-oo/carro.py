from veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, cor, rodas, marca,tanque):
        Veiculo.__init_(self, cor, rodas, marca,tanque)