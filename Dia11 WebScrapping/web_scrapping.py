import bs4
import requests

resultado = requests.get('https://escueladirecta-blog.blogspot.com/')
resultado2 = requests.get('https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html')
resultado3 = requests.get('https://www.udemy.com/user/fedegaray/')

soup = bs4.BeautifulSoup(resultado.text, 'lxml')
soup2 = bs4.BeautifulSoup(resultado2.text, 'lxml')
soup3 = bs4.BeautifulSoup(resultado3.text, 'lxml')

imagenes = soup3.select('img')[0]['src']
print(imagenes)

imagen_curso1 = requests.get(imagenes)

f = open('mi_imagen.svg', 'wb')
f.write(imagen_curso1.content)
f.close()
#for i in imagenes:
#    print(i)


# parrafo_especial = soup.select('a')[99].getText()
# columna_lateral = soup2.select('.section p')
# print(columna_lateral)


