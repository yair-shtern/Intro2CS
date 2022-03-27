#########################################################################
# FILE : shapes.py
# WRITER : Yair Shtern , yair.shtern , 318442241
# EXERCISE : intro2cs1 ex2 2020
# DESCRIPTION: A program that receives from the user an input
# that represent a shape (circle\rectangle\equilateral triangle)
# and returns shape area.
# We use auxiliary functions for calculate each shape.
#########################################################################

import math

def shape_area():
    ''' The funct gets from the user a number that represents a shape
    (1=circle, 2=rectangle, 3=triangle) and return is area
    using the following functions '''
    user_shape = float(input("Choose shape (1=circle, 2=rectangle, 3=triangle): "))
    if user_shape == 1:
        return calculate_circle()
    elif user_shape == 2:
        return calculate_rectangle()
    elif user_shape == 3:
        return calculate_triangle()
    else:
        return None


def calculate_circle():
    ''' The funct gets from the user a float that represents the radius
    of a circle and return is area'''
    circle_radius = float(input())
    return (math.pi * (circle_radius ** 2))

def calculate_rectangle():
    ''' The funct gets from the user two floats that represents two sides
    of a rectangle and return is area'''
    first_squares_side = float(input())
    second_squares_side = float(input())
    return first_squares_side * second_squares_side

def calculate_triangle():
    ''' The funct gets from the user a float that represents a side
    of a equilateral triangle and return is area'''
    triangle_side = float(input())
    return ((triangle_side ** 2) * (math.sqrt(3))/4)



