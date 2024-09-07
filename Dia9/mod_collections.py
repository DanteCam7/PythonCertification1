from collections import Counter
from collections import defaultdict
from collections import namedtuple

phrase = "al pan pan y al vino vino"
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 4, 1, 2, 5]
serie = Counter([1,1,1,1,1,1,2,2,2,2,2,7,7,7,7,7,7,7,7,7,7,4])
print(Counter(numeros))
print(Counter(phrase))
print(serie.most_common())
print(list(serie))

my_dicc = {'one':'green', 'two':'blue', 'three':'red'}
#si pido un elemento inexistente, truena el programa

my_dicc2 = defaultdict(lambda : 'nada')
my_dicc2['one'] = 'green'
print(my_dicc2['one'])
print(my_dicc2['two'])


Person = namedtuple('Person',['name','height','weight'])
ariel = Person('Ariel',1.76,79)

print(ariel)

