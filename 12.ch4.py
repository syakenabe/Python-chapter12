class Hexagon:
    def __init__(self, l):
        self.length = l

    def caluculate_perimeter(self):
        return self.length * 6

hexagon = Hexagon(6)

print(hexagon.caluculate_perimeter())
