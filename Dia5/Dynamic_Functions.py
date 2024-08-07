

def chequear_3_cifras (lista):

    lista1 = []

    for n in lista:
        if n in range(100,1000):
            lista1.append(n)
        else:
            pass
    return lista1

resultado = chequear_3_cifras([5504,4199,6000])
print(resultado)
print(type(resultado))

lista_numeros = [1, 50, 500, 5000, 750, 600]


def suma_menores(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if numero in range(1, 1000):
            suma += numero
        else:
            pass
    return suma

x = suma_menores(lista_numeros)
print(x)

lista_numeros = [1, 50, 500, 5000, 750, 600]
def suma_menores(lista):
    suma = 0
    for n in lista:
        if n in range (1,1000):
            suma += n
        else:
            pass
    return suma

y = suma_menores(lista_numeros)
print(y)