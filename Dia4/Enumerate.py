lista = ['a','b','c']


for item in enumerate(lista):
    print(item)

    #OR FOR A MORE LEGIBLE VIEW

for indice, item in enumerate(lista):
    print(indice,item)

mis_tuples = list(enumerate(lista))
print(mis_tuples[1][1])


lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')

lista_indices = list(enumerate("Python"))
cadena = 'Python'
lista2= list(cadena)
print(lista_indices)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice,letra in (lista_nombres):
    if letra[0] == 'M':
        print(indice)
