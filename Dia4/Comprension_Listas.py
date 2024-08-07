palabra = 'python'
lista = []

for letra in palabra:
    lista.append(letra)

print(lista)

###LO SIGUIENTE ES UNA MANERA MAS COMPRESA, MEJOR


lista2 = [letra for letra in 'palabra2']

print(lista2)

lista3 = [n for n in range(0,21,2)]
print(lista3)

lista4 = [n/2 for n in range(0,21,2)]
print(lista4)

lista5 = [n/2 for n in range(0,21,2) if n*2 > 10]
print(lista5)

lista6 = [n if n*2 > 10 else 'no' for n in range(0,21,2) ]
print(lista6)

pies = [10,20,30,40,50]
metros = [p * 3.281 for p in pies]
print(metros)


valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_pares = [val for val in valores if val%2 == 0 ]
print(valores_pares)

