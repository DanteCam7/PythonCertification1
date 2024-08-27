class Bird:

    alas = True

    def __init__(self, colour, species):
        self.colour = colour
        self.species = species

    def piar(self):
        print('pio, my colour is {}'.format(self.colour))

    def volar(self, metros):
        print(f"The bird flew {metros} meters")

piolin = Bird('yellow', 'canary')

piolin.volar(150)
piolin.piar()