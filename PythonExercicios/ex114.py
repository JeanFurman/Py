import requests
try:
    response = requests.get('http://pudim.com.br')
    print('\033[32mConsegui acessar o site do Pudim com sucesso!\033[m')
except:
    print('\033[31mO site pudim nao está acessivel no momento.\033[m')


