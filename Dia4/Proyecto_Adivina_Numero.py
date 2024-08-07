from random import *

intentos = 8
nombre = input('Hola, favor de escribir tu nombre jugador: ')

print('Ahora adivinarás un número entre el 1 y el 100')
num_secreto = randint(1,101)

while intentos > 0:
    numero = int(input('Inserta el número que creas: '))
    if numero > num_secreto:
        print('El número secreto es más bajo')
        intentos -= 1
    elif numero < num_secreto:
        print('El número secreto es más alto')
        intentos -= 1
    elif numero <= 0 or numero >100:
        print('El número secreto es entre 1 y 100')
        intentos -= 1
    elif numero == num_secreto:
        intentos -= 1
        print(f'LO LOGRASTE EN {8-intentos} intentos {nombre}, EL NUMERO ES {num_secreto}')
        break
    elif intentos == 0:
        print('Lamento informarte que perdiste, el número era: '+num_secreto)