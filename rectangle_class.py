class Rectangle:

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return round(self.width * self.height, 2)

    def perimeter(self) -> float:
        return round(2 * (self.width + self.height), 2)

    def s_square(self) -> bool:
        if self.width == self.height:
            return True
        else:
            return False

    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height

if __name__ == "__main__":

    r1 = Rectangle(10, 5)

    assert r1.area() == 50, "Test 1"
    assert r1.perimeter() == 30, "Test 2"
    assert r1.s_square() == False, "Test 3"
    r1.resize(12, 12)
    assert r1.s_square() == True, "Test 4"