import zipfile
import shutil

# mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')

# mi_zip.write('mi_texto_A.txt')
# mi_zip.write('mi_texto_B.txt')


# zip_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')
# zip_abierto.extractall()

# carpeta_origen = 'C:\\Users\\tejon\\Desktop\\YO'

# archivo_destino = 'Todo_Comprimido'

# shutil.make_archive(archivo_destino,'zip', carpeta_origen)

shutil.unpack_archive('Proyecto+Dia+9.zip', 'Extracción Completada', 'zip')
