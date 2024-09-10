import os
import shutil
import send2trash

print(os.getcwd())

archivo = open("curso.txt", 'w')
archivo.write('texto de prueba')
archivo.close()

print(os.listdir())

#shutil.move('curso.txt', "C:\\Users\\tejon\\Desktop")

#rmtree DELETES EVERYTHING IN THE ROUTE
#USE SEND2TRASH INSTEAD

send2trash.send2trash('curso.txt')

print(os.walk('C:\\Users\\tejon\\Desktop\\python\\pythonProject1'))

ruta = 'C:\\Users\\tejon\\Desktop\\python\\pythonProject1'

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpera: {ruta}')
    print(f'Las subcarpetas son:')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son:')
    for arch in archivo:
        print(f'\t{arch}')
    print('\n')


