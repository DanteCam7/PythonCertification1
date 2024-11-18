import bs4
import requests
import lxml


resultado = requests.get('https://shorturl.at/hMDOG')
resultado2 = requests.get('https://www.cyberpuerta.mx/Computo-Hardware/Componentes/Tarjetas-de-Video/Filtro/Procesador-grafico/GeForce-RTX-4060-Ti/?listorderby=oxvarminprice&listorder=asc')
sopa = bs4.BeautifulSoup(resultado2.text, 'lxml')

productos = sopa.find_all('div', class_='emproduct_right')
a = 1
for producto in productos:
    nombre = producto.find('a').text.strip()
    precio = producto.find('label').text.strip()
    print(f'{nombre} \n {precio}')
    a += 1
# print(producto)
# print(sopa.select('label'))

# producto_especifico = sopa.
# print(producto_especifico)

