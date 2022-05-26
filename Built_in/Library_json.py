import json
#Criando um arquivo JSON
lista = [1, 2, 3, 4, 5]

json.dumps(lista)

arq = open('teste.json', 'w')

json.dump(lista, arq)

arq.close()