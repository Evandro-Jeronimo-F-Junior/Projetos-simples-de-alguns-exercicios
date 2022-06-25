import requests
try:
    response = requests.get('https://google.com.br')
except:
    print('Deu erro')
else:
    print('deu certo')
