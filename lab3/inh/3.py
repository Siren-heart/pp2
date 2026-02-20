class Shape:
    def draw(self):
        print("Drawing a generic shape.")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle.")

class Square(Shape):
    def draw(self):
        print("Drawing a square.")

generic = Shape()
circle = Circle()
square = Square()

generic.draw()
circle.draw()
square.draw()