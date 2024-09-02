def my_function():
    list1 = []
    for x in range(1, 5):
        list1.append(x*10)
    return list1


def my_generator():
    for x in range(1,5):
        yield x * 10


print(my_function())
print(my_generator())

g = my_generator()

print(next(g))
print(next(g))
print(next(g))
print(next(g))

def my_generator2():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

g2= my_generator2()

print(next(g2))
print(next(g2))
print(next(g2))

