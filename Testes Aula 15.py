import requests
import json

acesso_dolar = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

# print(acesso_dolar.text)

dict_dolar = json.loads(acesso_dolar.text)

# print(dict_dolar['USDBRL'])
print('Moeda:', dict_dolar['USDBRL']['code'])
print('O valor mais alto do dólar hoje, em relação ao real brasileiro, foi:',dict_dolar['USDBRL']['high'])
print('O valor mais baixo do dólar hoje, em relação ao real brasileiro, foi:', dict_dolar['USDBRL']['low'])


# acesso_dolar_dict = json.loads(acesso_dolar)
#
# print(acesso_dolar_dict.text)
