class Point:
    def __init__(self, name, x, y):
        self.x = x
        self.y = y
        self.name = name

    def __str__(self):
        return f'{self.name}({self.x}, {self.y})'

    def __invert__(self):
        return Point(self.name, self.y, self.x)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return (self.x, self.y)


class ColoredPoint(Point):
    def __init__(self, name, x, y, colors=(0, 0, 0)):
        self.x = x
        self.y = y
        self.name = name
        self.colors = colors

    def get_color(self):
        return self.colors

    def __invert__(self):
        r, g, b = self.colors
        return ColoredPoint(self.name, self.y, self.x, (255 - r, 255 - g, 255 - b))


point_A = ColoredPoint('A', 0, 3, (255, 204, 0))
point_B = ColoredPoint('B', 5, -10)
print(point_A, point_A.get_coords(), point_A.get_color())
print(point_B, point_B.get_coords(), point_B.get_color())
