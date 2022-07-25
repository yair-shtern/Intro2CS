#########################################################################
# FILE : calculate_mathematical_expression.py
# WRITER : Yair Shtern
# EXERCISE : intro2cs1 ex2 2020
# DESCRIPTION: A simple program that calculate mathematical expression
# with to functions one receives two numbers and string (with the -
# mathematical action) and other receives a string with all the-
# mathematical expression
#########################################################################

def calculate_mathematical_expression(num1, num2, the_action):
    '''Check that the values are valid and calculate them'''
    if num2 == 0:
        return
    if the_action == '+':
        return num1+num2
    elif the_action == '-':
        return num1-num2
    elif the_action == '*':
        return num1*num2
    elif the_action == ':':
        return num1/num2
    else:
        return

def calculate_from_string(string):
    '''Split the string to num1, num2 and the action.
    and use the funct calculate_mathematical_expression to calculate'''
    string_action = string.split()
    num1 = float(string_action[0])
    num2 = float(string_action[2])
    the_action = string_action[1]
    return calculate_mathematical_expression(num1, num2, the_action)
