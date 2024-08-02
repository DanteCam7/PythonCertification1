mi_lista = ["a","b","c"]
mi_lista2 = ["d","e","f"]
otra_lsita = ["hola",55,455.6]

resultado = mi_lista[0:2]
print((resultado))

mi_lista3 = (mi_lista+mi_lista2)
mi_lista3.append("g")
#mi_lista3.pop() #sin parametro, elimina el ultimo, inserta indice
eliminado = mi_lista3.pop(5)

print(f"{mi_lista3}  se eliminó  {eliminado}")

lista = ['g','o','b','m','c']
lista.sort()    #NO SE PUEDE GUARDAR EN UNA VARIABLE, a menos que se haga lo siguiente
lista.reverse()
lista2 = lista
print(lista)




