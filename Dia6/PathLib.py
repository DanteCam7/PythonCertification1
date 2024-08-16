from pathlib import Path, PureWindowsPath

carpeta = Path('C:/Users/tejon/Desktop/python2/prueba.txt')
carpeta2 = Path('C:/Users/tejon/Desktop/python2/pruebas.txt')
print(carpeta.read_text())
print(carpeta.name)
print(carpeta.suffix)
print(carpeta.stem)

ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)

if not carpeta2.exists():
    print('Este archivo no existe')
else:
    print('Si existe, muy bien')

