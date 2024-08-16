archivo = open('prueba1.txt', 'w')
archivo.write('Soy UN TEXTO NUEVO \n')
archivo.write('Soy UN TEXTO SEMI-NUEVO \n')

archivo.writelines(['hola', 'mundo','aqui','estoy\n'])

lista = ['hola', 'mundo','aqui','estoy']

for p in lista:
    archivo.writelines(p + '\n')

archivo = open('prueba1.txt', 'a')
archivo.write('PRUEBA')

archivo.close()

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

registro = open("registro.txt", "a")
for item in registro_ultima_sesion:
    registro.writelines(item + '\t')

registro.close()
registro = open("registro.txt", "r")
print(registro.read())