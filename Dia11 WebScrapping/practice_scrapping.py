import bs4
import requests
# url base sin numero de pagina
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# lista de titulos con 4 o 5 estrellas
titulos_rating_ato = []

# iterar paginas
for pagina in range(1, 51):

    # crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    # iterar libros
    for libro in libros:

        # check 4 or 5 stars
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:

            # agregar titulo en variable
            titulo_libro = libro.select('a')[1]['title']

            # agregar a la lista
            titulos_rating_ato.append(titulo_libro)

# ver libros 4 o 5 estrellas en consola
for t in titulos_rating_ato:
    print(t)