class Triangle:
    def __init__(self, b, h):
        self.bottom = b
        self.height = h
        print("Craeted!!")

    def area(self):
        return self.bottom * self.height / 2

triangle = Triangle(10, 5)

print(triangle.area())
