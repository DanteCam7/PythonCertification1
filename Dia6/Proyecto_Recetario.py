import os
from pathlib import Path
from os import system
mi_ruta = Path(Path.home(), 'Recetas')

def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador

def inicio ():
    system('cls')
    print('*'*50)
    print("Bienvenido al Recetario")
    print('*'*50)
    print('\n')
    print(f'Las recetas se encuentra en {mi_ruta}')
    print(f'Total de recetas: {contar_recetas(mi_ruta)}')

    eleccion = 'x'
    while not eleccion.isnumeric() or eleccion not in range(1,7):
        print("Elige una opción: '")
        print('''
        [1] - Leer Receta
        [2] - Crear Receta
        [3] - Crear Categoría nueva
        [4] - Eleminar Receta
        [5] - Eliminar Categoría
        [6] - Salir del Programa
        ''')
        eleccion = input()
    return (eleccion)


inicio()


#Mostrar Menu inicio


menu = 0

if menu == 1:
    #mostrar categorias
    #elegir categoria
    #mostrar recetas
    #elegir recetas
    #leer receta
    pass
elif menu == 2:
    #mostrar categorias
    #elegir categoria
    #crear receta
    #volver inicio
    pass
elif menu == 3:
    #crear categoria
    #volver al inicio
    pass
elif menu == 4:
    # mostrar categorias
    # elegir categoria
    # mostrar recetas
    # elegir recetas
    #eleminar receta
    # leer receta
    pass
elif menu == 5:
    # mostrar categorias
    # elegir categoria
    #eleminar categoria
    #volver al inicio
    pass
elif menu == 6:
    #finalizar programa
    pass
