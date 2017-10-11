class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance(self, other):
        distance_x = self.x - other.x
        distance_y = self.y - other.y
        return Point(distance_x, distance_y)

    def move(self, x, y):
        self.x += x
        self.y += y

if __name__ == '__main__':
    self_point = Point(5, 5)

    if self_point == Point(5, 5):
        print("I work!")
    else:
        print("Wrong!")

    self_point.move(7, 9)
    print(self_point)
