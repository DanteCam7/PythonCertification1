import os

ruta = os.getcwd()
ruta2= os.chdir('C:\\Users\\tejon\\Desktop\\python2')
ruta3 =os.makedirs('C:\\Users\\tejon\\Desktop\\python2\\otra') #CREAR UNA CARPETA

archivo = open('prueba.txt')

print(archivo.read())

ruta4 = 'C:\\Users\\tejon\\Desktop\\python2\\prueba.txt'
elemento= os.path.basename(ruta4)
elemento2= os.path.dirname(ruta4)
elemento3 = os.path.split(ruta4)
print(elemento)
print(elemento2)
print(elemento3)

os.rmdir('C:\\Users\\tejon\\Desktop\\python2\\otra')

from pathlib import Path

carpeta = Path('C:/Users/tejon/Desktop/python2')
archivo = carpeta / 'prueba.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())