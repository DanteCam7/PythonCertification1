def suma (*args):
    return sum(args)

print(suma(5,6,4,4,5,8,3,38,8))


def suma_cuadrados (*args):
    suma = 0
    for arg in args:
        suma = suma + arg**2
    return suma

print(suma_cuadrados(1,2,3))