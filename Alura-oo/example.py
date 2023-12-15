import banco as b

matheus = b.Conta(56462,'matheus',500,1000)

roberta = b.Conta(946182,'roberta',500,1000)
#
# matheus.transfere(destino=roberta,valor=40)
#
# print(roberta.saldo())
# print(matheus.saldo())
#
# matheus.limite = 200
#
# print(f'O LIMITE = {matheus.titular} e TITULAR = {matheus.limite}')