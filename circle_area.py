"""
This program calculates the area of a circle
using a radius entered by the user.
"""

while True:
    try:
        radius = float(input("Enter the radius of the circle: "))

        if radius <= 0:
            print("Please enter a radius greater than 0.")
            continue

        area = 3.14 * radius ** 2

        print(f"The area of the circle is {area:.2f}")
        break

    except ValueError:
        print("Invalid input. Please enter a number.")
