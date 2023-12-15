import re #biblioteca para REGEX, ou Regular Expression

teste = 'O gato e gata e bonito'

procura = re.search(r'gat\w .',teste)
if  procura:
    print(procura)  # procura.group para mostrar apenas o texto
    print(procura.group())
    print('olá\ntudo bem?')
    print(r'olá\ntudo bem?')
else:
    print('Não achamos nada')

