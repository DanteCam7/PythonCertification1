import re

texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"

patron = 'ayuda'

busqueda = re.search(patron, texto)
busqueda2 = re.findall(patron, texto)
print(busqueda.span())
print(len(busqueda2))

for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())


texto2 = 'llama al 564-525-6588  ya mismo'

patron = re.compile(r'(\d{3})-(\d{3})-(\d{3})')

resultado2 = re.search(patron, texto2)
print(resultado2.group())


# clave = input('Clave: ')
clave = "a"
patron = r'\D{1}\w{7}'

chequear = re.search(patron, clave)
print(chequear)

texto = 'no atendemos los lunes y los martes'
buscar = re.search(r'....demos', texto)
buscar2 = re.findall(r'[^\s]+', texto)
print(buscar)
print(" ".join(buscar2))

#  ^ revisa si no hay lo que declaremos al inicio del string
# $ revisa que no haya un digito al final


def verificar_email(email):
    patron = r'@\w+\.com'
    verificar = re.search(patron,email)
    if verificar:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")


import re


def verificar_saludo(frase):
    patron = r'^Hola'
    verificar = re.search(patron, frase)
    if verificar:
        print("Ok")
    else:
        print("No has saludado")


import re


def verificar_cp(cp):
    patron = r'\w{2}\d{4}'
    verificar = re.search(patron, cp)
    if verificar:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")
