import csv
with open('numeros.csv', 'w', newline='') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(('nota1', 'nota2', 'nota3'))
    writer.writerow((63, 87, 92))
    writer.writerow((61, 79, 76))
    writer.writerow((72, 64, 91))
with open('numeros.csv', 'r', encoding='utf-8', newline='\r\n') as arquivo:
    leitor = csv.reader(arquivo)
    for x in leitor:
        print(x)

with open('numeros.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)
print(dados)
for linha in dados[1:]:
    print(linha)