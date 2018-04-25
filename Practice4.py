# Прямоугольная площадка (пример: комната) (свойства: две стороны)
# Нужно высчитать: площадь, периметр.

class Room:
    """This class describes rectangular room."""

    def __init__(self, length=0.0, width=0.0):
        self.length = length
        self.width = width

    def area(self):
        """This method returns the area of the room."""
        return self.length * self.width

    def perimeter(self):
        """This method returns the perimeter of the room."""
        return (self.length + self.width) * 2


l = float(input("Please enter the length of the room.\n"))
w = float(input("Please enter the width of the room.\n"))

r = Room(l, w)
print("The area of a room is {0:.2f}.".format(r.area()))
print("The perimeter of the room is {0:.2f}.".format(r.perimeter()))
