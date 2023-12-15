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
            # filme_info = requests.get(f'http://www.omdbapi.com/?s={filme}&apikey=d1224162')

        except Exception as erro:
            print('Ocorreu o erro: ')

        dicionario = json.loads(filme_info.text)
        lista = dicionario['Search']
        print(lista)
        # for i in lista:
        #     print(lista[])
        #     print()
        #     print()