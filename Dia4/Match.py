serie = "N-02"

match serie:
    case "N-01":
        print('Samsung')
    case 'N-02':
        print("Nokia")
    case 'N-03':
        print('Motorola')
    case _:
        print("No existe ese producto")

cliente = {'nombre': 'Federico',
           'edad' : 45,
           'ocupacion': 'instructor'}
pelicula ={'titulo': 'Matrix',
           'ficha_tecnica':{ 'protagonista': 'Keanu Reaves',
                             'director': 'Lana y Lillu Wachoswski'}}
elementos = [cliente,pelicula,'libro']

for e in elementos:
    match e:
        case{'nombre': nombre,
             'edad': edad,
             'ocupacion': ocupacion}:
            print('Es un cliente')
            print(nombre, edad, ocupacion)
        case{'titulo': titulo,
             'ficha_tecnica': {'protagonista': protagonista,
                               'director': director}}:
            print('Es una película')
            print(titulo, protagonista, director)
        case _:
            print("NO SE QUE ES ESTO")
