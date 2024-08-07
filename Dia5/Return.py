def multiplicar (num1,num2):
    total = num1*num2
    return total

resultado = multiplicar(5,10)
print(resultado)

def invertir_palabra(palabra):
    palabra = palabra[::-1]
    palabra = palabra.upper()
    return palabra

palabra = 'dante'
palabra = palabra[::-1]
print(palabra)
palabra = palabra.upper()