lista = ["a","c","d","e","f"]

for letra in lista:
    num_letra = lista.index(letra) + 1
    #print(f"Letra {num_letra}: {letra}")

lista2 = ['dante', 'juana', 'pedro', 'ivan', 'laura']

for nombre in lista2:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print('otro nombre')


numeros = [1,2,3,4,5,6,7]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero

print(mi_valor)


palabra = 'python'
for letra in palabra:
    print(letra)

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for alumno in alumnos_clase:
   print("Hola "+ alumno)