if 10 > 99:
    print('si')
else:
    print('no')

mascota='perro'
if mascota == 'gato':
    print('Gato')
elif mascota == 'perro':
    print('perro')
else:
    print('no sé que animal tienes')

edad = 16
calificacion = 9
if edad < 18:
    print('No eres adulto')
    if calificacion >= 7:
        print('aprobado')
    else:
        print('reprobado')
else:
    print('eres niño grande')