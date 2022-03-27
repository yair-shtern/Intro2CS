#########################################################################
# FILE : temperature.py
# WRITER : Yair Shtern , yair.shtern , 318442241
# EXERCISE : intro2cs1 ex2 2020
# DESCRIPTION: A program that gets 3 numbers which represent
# (max temperature, day1 temperature, day2 temperature, day3 temperature)
# and return True if in any  two of these three days the temperature
# was higher than the maximum temperature and False if if not
#########################################################################

def is_it_summer_yet(max_temp, day1_temp, day2_temp, day3_temp):
    '''We check if the max of any two days and the max temp is max temp
    return False else - returnTrue'''
    if (max(max_temp, day1_temp, day2_temp) == max_temp
    or max(max_temp, day1_temp, day3_temp) == max_temp
    or max(max_temp, day2_temp, day3_temp) == max_temp):
        return False
    else:
        return True

