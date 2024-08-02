diccionario = {'c1': 'valor1', 'c2': 'valor2'}
print(diccionario)
resultado = diccionario['c1']
print(resultado)

cliente = {'nombre': 'juan', "apellido": 'fuentes', 'peso': 54, 'talla': 1.56}
consulta = (cliente['apellido'])
print(consulta)

dic = {'c1': 55, 'c2': [10, 20, 30], 'c3': {'s1': 100, 's2': 200}}
print(dic['c2'][2])
print(dic['c3']['s2'])

dic2 = {'c1': ['a', 'b', 'c'], 'c2': ['d', 'e', 'f']}
print(dic2['c1'][0].upper())

dic3 = {1: 'a', 2: 'b'}
dic3[3] = 'c'
dic3[2] = 'B'
print(dic3)

print(dic3.keys())
print(dic3.values())
print(dic3.items())

mi_dic = {'nombre': 'Karen', 'apellido': 'Jurgens', 'edad': '35', 'ocupacion': 'Periodista'}
print(mi_dic)