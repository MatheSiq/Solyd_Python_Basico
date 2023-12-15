# application programming interface(API)
# JSON funciona igual a um dicionário no Python

import requests
import json

sair = 0

while sair == 0:
    escolha = int(input('deseja fazer o que? 1-pesquisar um filme 2-sair\n'))

    if escolha == 1:
        try:
            filme = str(input('Qual é o filme a ser pesquisado?\n'))
            print()
            filme_info = requests.get(f'https://www.omdbapi.com/?apikey=d1224162&t={filme}')

        except Exception as erro:
            print('Ocorreu o erro: ')
        dicionario = json.loads(filme_info.text)
        print(dicionario['Title'])
        print(dicionario['Year'])
        print(dicionario['Released'])
        print(dicionario['Runtime'])
        print(dicionario['Actors'])
        print(dicionario['Director'])
        print()
        print(dicionario1)

else:
    print('Obrigado por usar o programa')
    sair = 1