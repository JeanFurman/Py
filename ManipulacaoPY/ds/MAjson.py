dict_guido = {'nome': 'Guido van Rossum',
              'linguagem': 'Python',
              'similar': ['c', 'Modula-3', 'lisp'],
              'users': 1000000}
for k, v in dict_guido.items():
    print(k, v)

import json

print(json.dumps(dict_guido))
with open('dados.json', 'w') as arquivo:
    arquivo.write(json.dumps(dict_guido))

with open('dados.json', 'r') as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)
print(dados)
print(dados['nome'])
