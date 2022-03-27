#########################################################################
# FILE : largest_and_smallest.py
# WRITER : Yair Shtern , yair.shtern , 318442241
# EXERCISE : intro2cs1 ex2 2020
# DESCRIPTION: A simple program that receives three numbers and return
# two numbers first the largest and second the smallest
# mathematical action) and other receives a string with all the-
# mathematical expression
# In the funct check_largest_and_smallest I chose (0, 0, 0) to check
# if it works for 3 equal values and I chose (-4, 1, 4) to see
# if it differentiates between -a and a.
#########################################################################

def largest_and_smallest(num1, num2, num3):
    '''Check what is the largest number and then for each option,
    check what is smallest. and then return them'''
    if num1 >= num2 and num1 >=num3:
        largest = num1
        if num2 > num3:
            smallest = num3
        else:
            smallest = num2
    elif num2 >= num1 and num2 >= num3:
        largest = num2
        if num1 > num3:
            smallest = num3
        else:
            smallest = num1
    else:
        largest = num3
        if num1 > num2:
            smallest = num2
        else:
            smallest = num1
    return largest, smallest

def check_largest_and_smallest():
    '''Check if the largest_and_smallest funct works,
    by using end cases'''
    return( (largest_and_smallest(17, 1, 6) == (17, 1))
    and (largest_and_smallest(1, 17, 6) == (17, 1))
    and (largest_and_smallest(1, 1, 2) == (2, 1))
    and (largest_and_smallest(0,0,0) == (0, 0))
    and (largest_and_smallest(-4, 1, 4) == (4, -4)))


