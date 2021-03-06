from point import Point

class Rectangle:
    def __init__(self, width, height, top_left):
        self.width = width
        self.height = height
        self.top_left = top_left

    def __eq__(self, other):
        return self.w == other.w and self.h == other.h and self.tlp == other.tlp

    def __str__(self):
        return f"Rectangle({self.width}, {self.height}, {self.top_left})"

    def inside_point(self, point):
        return self.top_left.x <= point.x <= self.top_left.x + self.width and\
               self.top_left.y <= point.y <= self.top_left.y + self.height

    def center_point(self):
        return Point(self.width // 2, self.height // 2)

if __name__ == '__main__':

    rectangle = Rectangle(5, 10, Point(0, 0))

    print(rectangle.__str__())
    print(rectangle.inside_point(Point(4, 8)))
    print(rectangle.center_point())
