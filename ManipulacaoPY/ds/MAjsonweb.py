from urllib.request import urlopen
import json

response = urlopen('http://vimeo.com/api/v2/video/57733101.json').read().decode('utf8')
dados = json.loads(response)[0]
print(dados)
print('Titulo: ', dados['title'])
print('URL: ', dados['url'])
print('Duração: ', dados['duration'])
print('Numero de Visualizações: ', dados['stats_number_of_plays'])

arquivo_fonte = 'dados.json'
arquivo_destino = 'dados.txt'

# Método 1
with open(arquivo_fonte, 'r') as infile:
    text = infile.read()
    with open(arquivo_destino, 'w') as outfile:
        outfile.write(text)

# Método 2
open(arquivo_destino, 'w').write(open(arquivo_fonte, 'r').read())

with open('dados.txt', 'r') as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)

print(dados)
