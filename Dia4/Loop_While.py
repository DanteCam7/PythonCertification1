monedas = 5
while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:print("No tengo más dinero")

respuesta = 's'

while respuesta != 'n':
    respuesta = input('Quieres seguir? (s/n)')
else:
    print('Gracias')

#########################
while respuesta == 's':
    pass

print("hola")
######################

nombre = input("Tu nombre: ")

for letra in nombre:
    if letra == 'r':
        break#continue #break
    print(letra)

numero = 50

while numero >= 0:
   if numero%5 == 0:
       print(numero)
   numero -= 1