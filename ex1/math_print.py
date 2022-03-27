#################################################################
# FILE : math_print.py
# WRITER : Yair Shtern , yair.shtern , 318442241
# EXERCISE : intro2cs1 ex1 2020
# DESCRIPTION: A simple program that prints the result on
# a number of simple mathematical calculations.
#################################################################
import math
def golden_ratio():
    # Calculate and print the golden ratio.
    print ((1+math.sqrt(5))/2)


def six_squared():
    # Print 6 squared
    print(pow(6,2))


def hypotenuse():
    # Print the length of the hypotenuse in a right-angled triangle
    # whose sides are In lengths 12 and 5. calculate using Pythagoras
    print(math.sqrt(math.pow(5,2)+math.pow(12,2)))


def pi():
    # Print the number pi
    print(math.pi)


def e():
    # Print the number e
    print(math.e)


def squares_area():
    # Square areas(whose sides are 1, 2, 3, ..., 10)
    print(pow(1,2), pow(2,2), pow(3,2), pow(4,2),
          pow(5,2), pow(6,2), pow(7,2), pow(8,2), pow(9,2), pow(10,2))


if __name__ == "__main__" :
    golden_ratio()
    six_squared()
    hypotenuse()
    pi()
    e()
    squares_area()
