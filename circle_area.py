import math

def calculate_circle_area(radius: float) -> float:
         return round(math.pi * radius ** 2, 2)

while True:
    try:
        radius_circle = float(input("Enter the radius of the circle: "))
        print(calculate_circle_area(radius_circle))
        break
    except ValueError:
        print("Error! This is not a number. Try again.")
