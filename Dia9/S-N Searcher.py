import re
import os
import time
import datetime
from pathlib import Path
import math

route = 'C:\\Users\\tejon\\Desktop\\python\\pythonProject1\\Dia9\\Mi_Gran_Directorio'
mi_patron = r'N\D{3}-\d{5}'
hoy = datetime.date.today()
nros_encontrados = []
archivos_encontrados = []

inicio = time.time()


def buscar_numero(archivo, patron):
    este_archivo = open(archivo, 'r')
    text = este_archivo.read()
    if re.search(patron, text):
        return re.search(patron, text)
    else:
        return ''


def crear_listas():
    for carpeta, subcarpetas, archivo in os.walk(route):
        for a in archivo:
            resultado = buscar_numero(Path(carpeta, a), mi_patron)
            if resultado != '':
                nros_encontrados.append((resultado.group()))
                archivos_encontrados.append(a.title())


def mostrar_todo():
    indice = 0
    print('-' * 50)
    print(f'Fecha por Búsqueda: {hoy.day}/{hoy.year}/{hoy.year}')
    print('\n')
    print('ARCHIVO\t\t\tNRO. SERIE')
    print('-------\t\t\t----------')
    for a in archivos_encontrados:
        print(f'{a}\t{nros_encontrados[indice]}')
        indice += 1
    print('\n')
    print(f'Números encontrados: {len(nros_encontrados)}')
    fin = time.time()
    duracion = fin - inicio
    print(f'Duración de la búsqueda: {math.ceil(duracion)} segundos')
    print('-' * 50)


crear_listas()
mostrar_todo()
