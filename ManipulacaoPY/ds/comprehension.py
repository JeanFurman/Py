print([x for x in range(10)])
lista_n = [x for x in range(10)]
print(lista_n)
lista_n = [x for x in range(10) if x < 5]
print(lista_n)
lista_frutas = ['banana', 'acabate', 'melancia', 'cereja', 'manga', 'limao']
####FOR TRADICIONAL
new_list = []
for x in lista_frutas:
    if 'm' in x:
        new_list.append(x)
print(new_list)
####FOR COMPREHENSION
new_list = [x for x in lista_frutas if 'm' in x]
print(new_list)

####DICT COMPREHENSION
dict_alunos = {'Bob': 68, 'Michel':84, 'Zico': 57, 'Ana': 93}
dict_alunos_status = {k:v for (k,v) in dict_alunos.items()}
print(dict_alunos_status)
dict_alunos_status = {k: ('Aprovado' if v > 70 else 'Reprovado') for (k,v) in dict_alunos.items()}
print(dict_alunos_status)


