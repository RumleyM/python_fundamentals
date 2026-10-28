# Python Fundamentals - Circle Area Calculator

## Description
This Python program asks for user's name, performs basic string manipulation, and calculates the area of a circle based on a radius entered by the user.

The program uses the formula:

Area = 3.14 × radius²

## How to Run
1. Open `circle_area.py` in Python 3.
2. Run the program.
3. Enter your name when prompted.
4. Enter the radius of the circle when prompted.
5. The program will calculate and display the area.

## Input Validation
The program checks that the radius is a number greater than 0. If invalid input is entered, the program displays an error message and asks the user to try again.

## String Manipulation
The program uses `.strip()` to remove extra spaces from the user's name and `.title()` to format the capitalization. It also uses `len()` to count the number of characters in the formatted name.

## Testing
I tested the program with:
- A valid radius such as `5`
- A negative number such as `-5`
- Invalid text such as `abc`

## Assumptions
The radius must be greater than 0.
