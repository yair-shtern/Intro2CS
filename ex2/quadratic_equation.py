#########################################################################
# FILE : quadratic_equation.py
# WRITER : Yair Shtern , yair.shtern , 318442241
# EXERCISE : intro2cs1 ex2 2020
# DESCRIPTION: A program that solves a quadratic equation.
# The program receives from the user an input of 3 coordinates which -
# represent of the coefficients of the equation.
# When 'a' is the coefficient of X**2 b is coefficient of X
# and c is the free variable.
#########################################################################

import math

def quadratic_equation(a, b, c):
    ''' If there is no solution the funct returns (None, None),
    if there is one solution the funct returns (the solution, None)
    if there is two solutions the funct returns (solution num1, solution num2)'''
    if (b**2 -4*c*a) < 0:
        return None, None
    elif (b**2 -4*c*a) == 0:
        return -b  / (2 * a), None
    else:
        result1 = (-b + math.sqrt((b**2)-4*c*a))/(2*a)
        result2 = (-b - math.sqrt((b**2)-4*c*a))/(2*a)
        return result1, result2


def quadratic_equation_user_input():
    ''' If the user print 'a=0' he will receive an error message.
    Else, he will receive the result.
    We are using the funct "quadratic_equation" to get the results. '''
    user_input = input("Insert coefficients a, b, and c: ")
    user_input = user_input.split()
    a = float(user_input[0])
    b = float(user_input[1])
    c = float(user_input[2])
    if a == 0:
        print("The parameter 'a' may not equal 0")
        return
    results = quadratic_equation(a, b, c)
    result1 = results[0]
    result2 = results[1]
    if result1 == None and result2 == None:
        print("The equation has no solutions")
        return
    elif result1 != None and result2 == None:
        print("The equation has 1 solution:", result1)
        return
    else:
        print("The equation has 2 solutions:", result1, "and", result2)
        return

