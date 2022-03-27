########################################################################
# FILE : ex7.py
# WRITER : Yair Shtern , yair.shtern , 318442241
# EXERCISE : intro2cs1 ex7 2020
# DESCRIPTION: recursion functions
#######################################################################
from typing import Any, List, Tuple


def _print_to_n_helper(n: int, i: int) -> None:
    """
    Help func that print the numbers from 1 to n
    :param n: the last number to print
    :param i: index, run from 1 to n
    :return: None
    """
    if i == n + 1:
        return
    print(i)
    return _print_to_n_helper(n, i + 1)


def print_to_n(n: int) -> None:
    """
    A function that prints the numbers from 1 to n
    :param n: the last number to print
    :return: None
    """
    if n <= 0:
        return
    return _print_to_n_helper(n, 1)


def digit_sum(n: int) -> int:
    """
    Sum the digit of num n
    :param n: the number to sum his digit
    :return: int, the sum of the digit
    """
    if n <= 0:
        return 0
    else:
        return n % 10 + digit_sum(n // 10)


def has_divisor_smaller_than(n: int, i: int) -> bool:
    """
    Help func that checks if n has divisor smaller than i
    :param n: chek if it is divide
    :param i: check if i divide n
    :return: true if n has divisor smaller than i and else False
    """
    if i == 1:
        return False
    if n % i == 0:
        return True
    else:
        return has_divisor_smaller_than(n, i - 1)


def is_prime(n: int) -> bool:
    """
    Func that checks if n is a prime number
    :param n: the num to check
    :return: true if n is a prime and else False
    """
    if n <= 1:
        return False
    i = n // 2
    if has_divisor_smaller_than(n, i):
        return False

    return True


def play_hanoi(hanoi: Any, n: int, src: Any, dst: Any, temp: Any) -> None:
    """
    Play hanoi game. Moves n disks from src pole to the dts pole
    'ith this rules: It is allowed to move only one disc at a time
                     Do not place one disc on a small disc from her
    :param hanoi: the hanoi game
    :param n: the num of disks
    :param src: the source pole
    :param dst: the destination pole
    :param temp: the help pole
    :return: None
    """
    if n <= 0:
        return
    if n == 1:
        hanoi.move(src, dst)
        return
    play_hanoi(hanoi, n - 1, src, temp, dst)
    hanoi.move(src, dst)
    play_hanoi(hanoi, n - 1, temp, dst, src)


def _print_sequences_helper(char_list: List[str], n: int, string: str) -> None:
    """
    Help func that print sequences of strings
    :param char_list: the list of chars to make sequences of them
    :param n: the length of the string to print
    :param string: the string to print
    :return: None
    """
    if len(string) == n:
        print(string)
        return

    for i in char_list:
        _print_sequences_helper(char_list, n, string + i)


def print_sequences(char_list: List[str], n: int) -> None:
    """
    Func that prints every sequences of the chars in the list
    :param char_list: the list of chars to make sequences of them
    :param n: the length of the string to print
    :return: None
    """
    if n >= 0:
        return _print_sequences_helper(char_list, n, "")
    return


def char_not_in_string(char: str, string: str) -> bool:
    """
    Func that checks if char in string
    :param char: char in the list of chars
    :param string: the string to check if the char in it
    :return: True if char is in the string and else False
    """
    if string.find(char) != -1:
        return False
    return True


def _print_no_rep_helper(char_list: List[str], n: int, string: str) -> None:
    """
    Help func that print sequences of strings
    only if there is no repetitions
    :param char_list: the list of chars to make sequences of them
    :param n: the length of the string to print
    :param string: the string to print
    :return: None
    """
    if len(string) == n:
        print(string)
        return

    for char in char_list:
        if char_not_in_string(char, string):
            _print_no_rep_helper(char_list, n, string + char)


def print_no_repetition_sequences(char_list: List[str], n: int) -> None:
    """
    Func that prints every sequences of the chars in the list
    but with no repetitions of chars
    :param char_list: the list of chars to make sequences of them
    :param n: the length of the string to print
    :return: None
    """
    if n >= 0:
        return _print_no_rep_helper(char_list, n, "")
    return


def _parentheses_helper(n: int, lst: List[str], string: str) -> None:
    """
    Help func which adds to the list every legal sequences
    of parentheses in the length of n * 2
    :param n: the number of couple of parentheses
    :param lst: the parentheses list
    :param string: the current string
    :return: None
    """
    if len(string) < 2 * n - 1:
        _parentheses_helper(n, lst, string + "(")

    if string.count("(") == string.count(")") == n:
        lst.append(string)
        return

    if string.count("(") > string.count(")"):
        _parentheses_helper(n, lst, string + ")")


def parentheses(n: int) -> List[str]:
    """
    Function that gets a non-negative integer n
    and returns a list with all the strings with n valid pairs of parenthesis
    In each initial of the string the number of characters '('
    greater than or equal to the number of characters ')'
    and the number of characters of each type in the entire string is equal.
    :param n: the num of pairs of parenthesis
    :return: list of pairs of parenthesis
    """
    if n <= 0:
        return [""]
    lst: List[str] = []
    _parentheses_helper(n, lst, "")
    return lst


def _flood_fill_helper(image: List[List[str]],
                       start: Tuple[int, int], row: int, col: int) -> None:
    """
    Help func that replaces the characters "."
    with the characters "*" starting from the starting point.
    :param image: the array to change
    :param start: the starting point
    :param row: the current row we in
    :param col: the current col we in
    :return: None
    """
    if image[row][col] == "*":
        return
    image[row][col] = "*"  # image[row][col] == "."

    _flood_fill_helper(image, start, row - 1, col)
    _flood_fill_helper(image, start, row + 1, col)
    _flood_fill_helper(image, start, row, col - 1)
    _flood_fill_helper(image, start, row, col + 1)


def flood_fill(image: List[List[str]], start: Tuple[int, int]) -> None:
    """
    Func that replaces in the array 'image' the characters "."
    with the characters "*" starting from the starting point.
    At any given moment, we are only allowed to fill an empty cell
    if it is the cell marked start, or if it is next to the cell
    which was filled earlier.
    We will define cells as adjacent only if they are to the right,
    left, above or below each other (and not if they are diagonal).
    :param image: the array to change
    :param start: Tuple that represents the starting point
    :return: None
    """
    return _flood_fill_helper(image, start, start[0], start[1])
