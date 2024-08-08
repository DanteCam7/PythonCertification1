# EXCERCISE 1
def devolver_distintos(num1,num2,num3):
    lista = [num1,num2,num3]
    suma= num1+num2+num3
    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort()
        return lista [1]
print(devolver_distintos(9,2,3))

# EXCERCISE 2
def palabras (palabra):
    mi_set = set()
    for letra in palabra:
        mi_set.add(letra)

    lista = list(mi_set)
    lista.sort()

    return lista
print(palabras('DANTE'))


# EXCERCISE 3

def argumentos (*args):
    count = 0
    for arg in args:
        if count + 1 == len(args):
            return False
        elif args[count] == 0 and args[count +1] == 0:
            return True
        else:
            count += 1
    return False

print(argumentos(1,2,3,4,0,5,6,7,8,9,0))


#EXCERCISE 4

def contar_primos(num1):
    primos = [2]
    iteracion = 3

    if num1 < 2:
        return 0

    while iteracion <= num1:
        for n in range(3,iteracion,2):
            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion += 2

    print(primos)
    return len(primos)

print(contar_primos(30))
