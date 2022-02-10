import math


class Rectangle:
    def __init__(self, _width, _height):
        self.width = _width
        self.height = _height

    def set_width(self, _width):
        self.width = _width

    def set_height(self, _height):
        self.height = _height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_area(self):
        return self.width * self.height

    def get_diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)

    def get_string(self):
        return type(self).__name__ + '(width=' + str(self.width) + ', height=' + str(self.height) + ')'

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture"
        outPut = [['*'] * self.width] * self.height
        return self.get_string() + '\n' + '\n'.join(map(''.join, outPut))

    def get_amount_inside(self, name):
        return math.ceil(float(self.get_area()) / float(name.get_area()))


class Square(Rectangle):
    def __init__(self, width):
        super(Square, self).__init__(_width=width, _height=width)

    def set_side(self, _width):
        self.width = _width
        self.height = _width

    def get_string(self):
        return type(self).__name__ + '(side=' + str(self.width) + ')'


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
print(sq.get_perimeter())
sq.set_side(4)
print(sq.get_diagonal())
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))