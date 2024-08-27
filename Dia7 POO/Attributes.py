class Bird:

    alas = True
    def __init__(self, colour,species):
        self.colour = colour
        self.species = species


my_bird = Bird('Green', 'Tucan')

print(f"My {my_bird.species} is {my_bird.colour}, and has wings {Bird.alas}")


##############################    EXCERSISES  ###############################
class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos

casa_blanca = Casa('blanco', 4)


class Cubo:
    caras = 6

    def __init__(self, color):
        self.color = color


cubo_rojo = Cubo("rojo")


