#IDADE,PESO,ALTURA da pessoa e decidir se está apto a entrar no exercíto (+18 anos, +=60kilos +=1,70m)

idade = int(input("Qual é sua idade?"))
peso = float(input("Qual é o seu peso?"))
altura = float(input("Qual é a sua altura?"))

if idade >= 18 and peso >= 60 and altura >= 1.70:
    print("Parabéns, você está apto a entrar no exécito")
else:
    print("Infelizmente você não está apto a entrar no exécito")