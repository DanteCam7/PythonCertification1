mi_lista = [1,1,1,1,1,1,1]
print((mi_lista))

class Object:
    pass

my_object = Object()
print((my_object))


class CD:

    def __init__(self, author, title, songs):
        self.author = author
        self.title = title
        self.songs = songs

    def __str__(self):
        return f"Album: {self.title} of {self.author}"

    def __len__(self):
        return self.songs

    def __del__(self):
        print("The CD has been deleted")

my_cd = CD('Pink Floyd', 'The Wall', 24)
print(my_cd)
print(len(my_cd))

#del my_cd      #ERRASE INSTANCE


