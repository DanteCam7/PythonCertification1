class Animal:

    def __init__(self,age, colour, species):
        self.age = age
        self.colour = colour
        self.species = species

    def born(self):
        #self.animal = animal
        print(f"This {self.species} has born")


class Bird(Animal):
    pass

print(Bird.__bases__)
print(Animal.__subclasses__())

piolin = Bird(3, 'red', 'Tucan')

piolin.born()