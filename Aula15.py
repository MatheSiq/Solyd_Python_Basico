#Essa aula é destinada a dois exercícios.
#Primeiramente é necessário fazer um app que trás a cotação do dolar
#Por fim é preciso criar um app que trás a previsão do tempo
import requests
import json

cond = 1

while cond == 1:
    print('1- Cotação do dólar')
    print('2- Clima')
    print('3- Sair')
    escolha = input('Você deseja saber a cotação do dólar ou a previsão do tempo em uma localidade?\nDigite 1, 2 ou 3: ')

    if escolha == '1':

        acesso_dolar = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

        dict_dolar = json.loads(acesso_dolar.text)
        print()
        print()
        print('Moeda:', dict_dolar['USDBRL']['code'])
        print('O valor mais alto do dólar hoje, em relação ao real brasileiro, foi:', dict_dolar['USDBRL']['high'])
        print('O valor mais baixo do dólar hoje, em relação ao real brasileiro, foi:', dict_dolar['USDBRL']['low'])
        print()
        print()

    elif escolha == '2':

        print()
        estado = input('Em qual estado está localizada a cidade que você quer saber o clima?\n')
        cidade = input('Escreva o nome da Cidade que você deseja saber o Clima\n')
        countrycode = '+55'

        acesso = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={cidade},{estado},{countrycode}&appid=eef95a70246c35d1caf44acf5ad67616')

        coords = json.loads(acesso.text)

        nome = coords[0]["name"]
        latitude = coords[0]["lat"]
        longitude = coords[0]["lon"]

        clima = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=eef95a70246c35d1caf44acf5ad67616')

        main_data = json.loads(clima.text)
        # print(main_data['weather'])
        atual = int(main_data['main']['temp']) - 273.15
        maxima = int(main_data['main']['temp_max']) - 273.15
        minima = int(main_data['main']['temp_min']) - 273.15
        sensacao = int(main_data['main']['feels_like']) - 273.15

        atual_s = str(atual)
        maxima_s = str(maxima)
        minima_s = str(minima)
        sensacao_s = str(sensacao)

        print(f'A temperatura atual é: {atual}')
        print(f'A sensação térmica é: {sensacao}')
        print(f'A temperatura mínima de hoje é: {minima}')
        print(f'A temperatura máxima de hoje é: {maxima}')
        print()

    elif escolha == '3':
        print('Obrigado por usar o programa')
        break