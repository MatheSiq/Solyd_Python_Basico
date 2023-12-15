from veiculo import Veiculo

Carro = Veiculo('verde','2','Ford','24L')
print(f"O carro possui",Carro.rodas,"rodas, sua cor dominante é",Carro.cor,"e ele é da marca",Carro.marca,"e por fim, seu tanque possui",Carro.tanque)

# Exercicio
# Crie um software de gerenciamento bancario
# Cada cliente precisa de um nome, cpf,idade
# Cada conta possui um cliente,saldo,limite negativo, e possui os metodos sacar,depositar e consultar saldo.