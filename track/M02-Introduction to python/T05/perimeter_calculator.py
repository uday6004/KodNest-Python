class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


class Square:
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side


# Reading the inputs (length, breadth, and side on separate lines)
rect_length = int(input())
rect_breadth = int(input())
square_side = int(input())

# Creating one object of each class
rect = Rectangle(rect_length, rect_breadth)
sq = Square(square_side)

# Storing both objects in a list
shapes = [rect, sq]

# Calling perimeter() on each object using a loop and printing the result
for shape in shapes:
    print(shape.perimeter())