########################################################################
# FILE : wave_editor.py
# WRITERS : Yair Shtern, David Zuravin
# EXERCISE : intro2cs1 ex6 2020
# DESCRIPTION: A wave files program.
# The program allows the user to make changes and create web files
# (the default sample rate will be 2000)
########################################################################
from os import path
from wave_helper import *
import math


MAX_VOLUME = 32767
MIN_VOLUME = -32768
DEFAULT_SAMPLE_RATE = 2000
SAMPLE_TIME = 1 / 16
DEFAULT_SAMPLES_PER_CYCLE = 125
FREQUENCY = {'A': 440,'B': 494,'C': 523,
             'D': 587,'E': 659,'F': 698,'G': 784,'Q': 0}


def valid_input(get_input):
    """
    Check if the input enters at the main menu is valid
    :param get_input: the input enters by the user
    :return: True if valid else, False
    """
    if get_input != '1' and \
            get_input != '2' and \
            get_input != '3':
        print('Invalid input try again')
        return False
    return True


def valid_operation(user_operation):
    """
    Check if the input enters at the modification menu is valid
    :param user_operation: the input enters by the user
    :return: True if valid else, False
    """
    if len(user_operation) == 1 and \
            48 < ord(user_operation) < 57:
        return True
    return False


def reverse(wave_list):
    """
    Reverse operation - reverse the audio
    :param wave_list: the melody list to change
    :return: the changed list
    """
    new_wave_list = [wave_list[0],[]]
    for i in range(len(wave_list[1]) - 1,-1,-1):
        new_wave_list[1].append(wave_list[1][i])
    return new_wave_list


def audio_negation(wave_list):
    """
    Audio negation operation - negates the audio
    :param wave_list: the melody list to change
    :return: the changed list
    """
    new_wave_list = [wave_list[0],[]]
    for i in range(len(wave_list[1])):
        new_wave_list[1].append([wave_list[1][i][0] * -1,
                                 wave_list[1][i][1] * -1])
    return new_wave_list


def speed_up(wave_list):
    """
    Speeds up the audio
    :param wave_list: the melody list to change
    :return: the changed list
    """
    new_wave_list = [wave_list[0],[]]
    for i in range(len(wave_list[1])):
        if i % 2 == 0:
            new_wave_list[1].append(wave_list[1][i])
    return new_wave_list


def slow_down(wave_list):
    """
    Slows down the audio
    :param wave_list: the melody list to change
    :return: the changed list
    """
    new_wave_list = [wave_list[0],[]]
    for i in range(len(wave_list[1])):
        new_wave_list[1].append(wave_list[1][i])
        if i < len(wave_list[1]) - 1:
            new_wave_list[1].append(
                [int((wave_list[1][i][0] + wave_list[1][i + 1][0]) / 2),
                 int((wave_list[1][i][1] + wave_list[1][i + 1][1]) / 2)])
    return new_wave_list


def make_pair(int_left,int_right):
    """
    A help func that make pairs in a melody
    that has increased or decreased the volume
    :param int_left: the left index in the pair
    :param int_right: the right index in the pair
    :return: list withe the pair
    """
    new_pair = []
    if MAX_VOLUME >= int_left >= MIN_VOLUME:
        new_pair.append(int_left)
    elif int_left > MAX_VOLUME:
        new_pair.append(MAX_VOLUME)
    else:
        new_pair.append(MIN_VOLUME)
    if MAX_VOLUME >= int_right >= MIN_VOLUME:
        new_pair.append(int_right)
    elif int_right > MAX_VOLUME:
        new_pair.append(MAX_VOLUME)
    else:
        new_pair.append(MIN_VOLUME)
    return new_pair


def volume_up(wave_list):
    """
    Increases the audio volume
    :param wave_list: the melody list to change
    :return: the changed list
    """
    new_wave_list = [wave_list[0],[]]
    for i in range(len(wave_list[1])):
        int_left = int(wave_list[1][i][0] * 1.2)
        int_right = int(wave_list[1][i][1] * 1.2)
        new_wave_list[1].append(make_pair(int_left,int_right))
    return new_wave_list


def volume_down(wave_list):
    """
    Decrease the audio volume
    :param wave_list: the melody list to change
    :return: the changed list
    """
    new_wave_list = [wave_list[0],[]]
    for i in range(len(wave_list[1])):
        int_left = int(wave_list[1][i][0] / 1.2)
        int_right = int(wave_list[1][i][1] / 1.2)
        new_wave_list[1].append(make_pair(int_left,int_right))
    return new_wave_list


def low_pass_filter(wave_list):
    """
    Blur the audio by a low pass filter
    :param wave_list: the melody list to change
    :return: the changed list
    """
    new_wave_list = [wave_list[0],[]]
    for i in range(len(wave_list[1])):
        if 0 == i < len(wave_list[1]) - 1:
            # index in lst[0] and the len of the list > 0
            new_wave_list[1].append(
                [int((wave_list[1][0][0] +
                      wave_list[1][1][0]) / 2),
                 int((wave_list[1][0][1] +
                      wave_list[1][1][1]) / 2)])
        elif i < len(wave_list[1]) - 1:
            # index not in the start or in the end of the list
            new_wave_list[1].append(
                [int((wave_list[1][i - 1][0] +
                      wave_list[1][i][0] +
                      wave_list[1][i + 1][0]) / 3),
                 int((wave_list[1][i - 1][1] +
                      wave_list[1][i][1] +
                      wave_list[1][i + 1][1]) / 3)])
        elif i > 0:
            # index in the end of the list and index > 0
            new_wave_list[1].append(
                [int((wave_list[1][i - 1][0] +
                      wave_list[1][i][0]) / 2),
                 int((wave_list[1][i - 1][1] +
                      wave_list[1][i][1]) / 2)])
        else:
            # len of the list is 1 / 0
            new_wave_list[1].append(wave_list[1][i])
    return new_wave_list


def operations(wave_list,user_operation):
    """
    make the requested change on the wave list
    :param wave_list: the melody list to change
    :param user_operation: the num of operation to make
    :return: the changed wave list
    """
    if user_operation == '1':
        wave_list = reverse(wave_list)
    elif user_operation == '2':
        wave_list = audio_negation(wave_list)
    elif user_operation == '3':
        wave_list = speed_up(wave_list)
    elif user_operation == '4':
        wave_list = slow_down(wave_list)
    elif user_operation == '5':
        wave_list = volume_up(wave_list)
    elif user_operation == '6':
        wave_list = volume_down(wave_list)
    elif user_operation == '7':
        wave_list = low_pass_filter(wave_list)
    return wave_list


def read_wav_file():
    """
    If the user enters e valid file
    a list represents the melody will create
    :return: wave list
    """
    while True:
        file_to_read = input('Please enter the file '
                             'name that you wont to modify')
        wave_list = load_wave(file_to_read)
        if wave_list == -1:
            print('Invalid file')
            continue
        else:
            break
    return wave_list


def modification_menu(wave_list):
    """
     Displays the modification menu to the user.
     When he enters a valid input the requested change will create
    :param wave_list: the melody list to change
    """
    while True:
        user_operation = input('Enter 1 to reverse the audio.\n '
                               '2 to negate the audio.\n '
                               '3 to speed up the audio.\n '
                               '4 to slow down the audio.\n '
                               '5 to turn up the volume.\n '
                               '6 to turn down the volume.\n '
                               '7 to create low pass filter.\n '
                               '8 for end menu')
        if not valid_operation(user_operation):
            print('Invalid input choose number between 1-8')
            continue
        elif user_operation == '8':
            exit_menu(wave_list)
            break
        else:
            wave_list = operations(wave_list,user_operation)
    main_menu()


def exit_menu(wave_list):
    """
    Saved the result in a file and exit to the main menu
    :param wave_list: the melody ist
    """
    file_saved = -1
    while file_saved == -1:
        file_to_save = input('Enter the file name to save.')
        file_saved = save_wave(wave_list[0],wave_list[1],file_to_save)
        if file_saved == 0:
            break
        else:
            print('There was a problem try again')
            continue


def make_composition_list(chars_list):
    """
    create the composition list from the chars list
    :param chars_list: chars that represent the melody
    :return: composition list
    """
    composition_list = [DEFAULT_SAMPLE_RATE,[]]
    for i in range(0,len(chars_list),2):
        for j in range(int(chars_list[i + 1]) * DEFAULT_SAMPLES_PER_CYCLE):
            sample = make_sample(FREQUENCY[chars_list[i]],j)
            composition_list[1].append([int(sample),int(sample)])
    return composition_list


def make_sample(sample_frequency,j):
    """
    create the sample for each pair
    :param sample_frequency: the sample frequency
    :param j: num of samples
    :return: sample
    """
    if sample_frequency == 0:
        return 0
    else:
        return MAX_VOLUME * \
               math.sin(math.pi * 2 *
                        (j / (DEFAULT_SAMPLE_RATE /
                              sample_frequency)))


def compose_melody_operation(composition_file):
    """
    Reda from the file chars that represent the
    melody and create a list of chars
    :param composition_file: the file to create the
    composition list from
    :return: composition list
    """
    chars_list = []
    with open(composition_file,'r') as file_to_modify:
        for line in file_to_modify:
            chars_list += line.split()
    composition_list = make_composition_list(chars_list)
    return composition_list


def compose_melody():
    """
     compose melody.
     If the user enters an existing file
     the func will return a list representing the melody
    """
    while True:
        melody_file = input('Enter the composition '
                            'guidelines file name.')
        if not path.isfile(melody_file):
            print('File not exists try again')
            continue
        else:
            break
    composition_list = compose_melody_operation(melody_file)
    return composition_list


def main_menu():
    """
     The home menu.
     Displays the main menu to the user.
     When he enters a valid input
     (1 to modify file, 2 to compose a melody, 3 for exit)
     he will go to the requested func
    """
    val_input = False
    while not val_input:
        get_input = input('Enter 1 to modify a wav file.\n '
                          '2 to compose a melody.\n '
                          '3 to exit from the program.')
        val_input = valid_input(get_input)
        if not val_input:
            continue
        if get_input == '3':
            break
        else:
            if get_input == '1':
                wave_list = read_wav_file()
            else:  # input == '2'
                wave_list = compose_melody()
        modification_menu(wave_list)


if __name__ == '__main__':
    main_menu()
