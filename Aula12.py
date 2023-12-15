import requests

try:
    req = requests.get('http://google.com')
    print(req)
    print(req.text)
except Exception as erro:
    print("Ocorreu o erro", erro)

    # Estudar biblioteca requests