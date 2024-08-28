class Animal:

    def __init__(self,age, colour):
        self.age = age
        self.colour = colour

    def born(self):
        #self.animal = animal
        print(f"This animal has born")

    def talk(self):
        print("This animal makes a sound")


class Bird(Animal):

    def __init__(self, age, colour, fly_height):
        super().__init__(age,colour)
        self.fly_height = fly_height

    def talk(self):
        print('pio')

    def fly(self,meters):
        print(f'The {self.colour} bird flies {meters} meters')

piolin = Bird(3, 'red', 150)
my_animal = Animal(5, 'black')

piolin.fly(150)

###################################################################################################

class Father:
    def talk(self):
        print("Hello")

class Mother():
    def laugh(self):
        print("ha ha")

    def talk(self):
        print("How r u?")

class Son(Father, Mother):
    pass

class Grandson(Son):
    pass

my_grandson = Grandson()

my_grandson.talk()
my_grandson.laugh()

print(Grandson.mro())