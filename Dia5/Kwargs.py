def prueba(num1,num2, *args, **kwargs):

    print(f'El primer valor es {num1}')
    print(f'El segundo valor es {num2}')

    for arg in args:
        print(f'arg = {arg}')



    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")


args = [351,35,153,4,3544,2,4,24]
kwargs = {'x':'uno','y':'dos','z':'tres'}

prueba(15,50,*args, **kwargs)




def cantidad_atributos(**kwargs):
    cantidad = 0
    for clave in kwargs.items():
        cantidad += 1
    return cantidad


def lista_atributos(**kwargs):
    lista = []
    for valor in kwargs.values():
        lista.append(valor)
    return lista


def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')
