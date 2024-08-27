class Bird:

    alas = True

    def __init__(self, colour, species):
        self.colour = colour
        self.species = species

    def piar(self):
        print('pio, my colour is {}'.format(self.colour))

    def volar(self, metros):
        print(f"The bird flew {metros} meters")
        self.piar()

    def paint_black(self):
        self.colour = 'negro'
        print(f"Now the bird is {self.colour}")

    @classmethod
    def put_eggs(cls, quantity):
        print(f"He put {quantity} eggs")
        cls.alas = False
        print(f"Alas {Bird.alas}")

    @staticmethod
    def watch():
        print("The bird watch")

piolin = Bird('yellow', 'canary')

piolin.volar(150)
piolin.paint_black()
piolin.alas = False
print(piolin.alas)
Bird.watch()

Bird.put_eggs(5)