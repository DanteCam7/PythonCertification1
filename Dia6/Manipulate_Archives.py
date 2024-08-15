mi_archivo = open("prueba.txt")
mi_archivo2 = open("prueba.txt")
mi_archivo3 = open("prueba.txt")

print("\n " + mi_archivo.readline().upper() )
print("\n " + mi_archivo.readline().rstrip())
print("\n " + mi_archivo.readline())


for linea in mi_archivo2:
    print('Aquí dice:' + linea)

todas = mi_archivo3.readlines()
todas = todas.pop()
print(todas)


mi_archivo.close()