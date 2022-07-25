########################################################################
# FILE : wordsearch.py
# WRITER : Yair Shtern
# EXERCISE : intro2cs1 ex5 2020
# DESCRIPTION: word search.
# A program that receives from the command line 4 parameters.
# The first is a name of file of words
# The first is a name of file that represent matrix:
# (Lines of same length with letters)
# The third is a name of file to write the result
# The fours is a string of letters that represent
# directions for searching in the matrix.
# (u=up,d=down,r=right,l=left,w=right up diagonal,x=left up diagonal
# y=right down diagonal,z=left down diagonal)
# The program returns a file (named as a parameter) with the words that
# appeared in the matrix and the number of occurrences
#######################################################################
import os.path
import sys


def read_wordlist(filename):
    """
    Read word list from file
    :param: filename: name of file to read from
    :return: list of word from the file
    """
    word_list = []
    with open(filename,'r') as f:
        for line in f:
            word_list.append(line.strip())
    return word_list


def read_matrix(filename):
    """
    Read matrix from file
    :param: filename: name of file to read from
    :return: list of list withe letters that represent matrix
    """
    mat = []
    with open(filename,'r') as f:
        for line in f:
            mat.append(line.strip().split(','))
    return mat


def write_output(result,filename):
    """
    Write result file with words found in matrix
    :param: filename: name of file to write in to
    :param: result: result list to write
    """
    with open(filename,'w') as file:
        for i in range(len(result)):
            output = str((result[i][0]) + ',' + str(result[i][1]))
            file.write(output + '\n')
    return


def correct_num_of_args(arguments):
    """
    Check if num of arguments is correct
    :return: False if not and True False
    """
    if len(arguments) != 5:
        print('Error! wrong number of arguments')
        return False
    return True


def files_exists(word_list_file,matrix_file):
    """
    Check if files given to read are exists
    :param: word_list_file: file represent the matrix
    :param: matrix_file: file represent the matrix
    :return: True if its ok and else False and print informative message
    """
    if not os.path.isfile(word_list_file):
        print('Error! the word list file is not exists')
        return False
    elif not os.path.isfile(matrix_file):
        print('Error! the matrix file is not exists')
        return False
    else:
        return True


def valid_input(directions):
    """
    Check if string given is valid
    :param: directions: string represent the directions to search in matrix
    :return: True if its ok and else False and print informative message
    """
    for i in directions:
        if i != 'u' and i != 'd' and i != 'r' and i != 'l' and i != 'w' and \
                i != 'x' and i != 'y' and i != 'z':
            print("Error! invalid input")
            return False
    return True


def count_word(word,string):
    """
    Count the appearance of word in string (at list 1)
    :param: word: a word to search in string
    :param: string: a string
    :return: the count of appearance of word in string
    """
    count = 1
    short_string = string[string.find(word) + 1:]
    while string != '':
        if word in short_string:
            count += 1
            short_string = short_string[short_string.find(word) + 1:]
        else:
            break
    return count


def check_and_update(result_dict,string,word_list):
    """
    Check if word in a string and update in the result dict
    :param: result_dict: a dict with the result of the word founds so far
    :param: string: a string
    :param: word_list: a list of word to check if in the string
    :return: None
    """
    for word in word_list:
        if word in string:
            if word in result_dict:
                result_dict[word] += count_word(word,string)
            else:
                result_dict[word] = count_word(word,string)
    return


def check_up(result_dict,word_list,matrix):
    """
    Check if words in the matrix in direction - up
    :param: result_dict: a dict with the result of the word founds so far
    :param: word_list: a list of words
    :param: matrix: a matrix to check on
    :return: the updated dict
    """
    for j in range(len(matrix[0])):
        i = len(matrix) - 1
        string = ''
        while i >= 0:
            string += matrix[i][j]
            i -= 1
        check_and_update(result_dict,string,word_list)
    return result_dict


def check_down(result_dict,word_list,matrix):
    """
     Check if words in the matrix in direction - down
     :param: result_dict: a dict with the result of the word founds so far
     :param: word_list: a list of words
     :param: matrix: a matrix to check on
     :return: the updated dict
     """
    for j in range(len(matrix[0])):
        i = 0
        string = ''
        while i < len(matrix):
            string += matrix[i][j]
            i += 1
        check_and_update(result_dict,string,word_list)
    return result_dict


def check_right(result_dict,word_list,matrix):
    """
     Check if words in the matrix in direction - right
     :param: result_dict: a dict with the result of the word founds so far
     :param: word_list: a list of words
     :param: matrix: a matrix to check on
     :return: the updated dict
     """
    for i in range(len(matrix)):
        string = ''
        for j in range(len(matrix[0])):
            string += matrix[i][j]
        check_and_update(result_dict,string,word_list)
    return result_dict


def check_left(result_dict,word_list,matrix):
    """
     Check if words in the matrix in direction - left
     :param: result_dict: a dict with the result of the word founds so far
     :param: word_list: a list of words
     :param: matrix: a matrix to check on
     :return: the updated dict
     """
    for i in range(len(matrix)):
        string = ''
        for j in range((len(matrix[0]) - 1),-1,-1):
            string += matrix[i][j]
        check_and_update(result_dict,string,word_list)
    return result_dict


def check_right_up(result_dict,word_list,matrix):
    """
     Check if words in the matrix in direction - right diagonal up
     :param: result_dict: a dict with the result of the word founds so far
     :param: word_list: a list of words
     :param: matrix: a matrix to check on
     :return: the updated dict
     """
    index1 = len(matrix) - 1
    while index1 >= 0:
        str1 = right_diagonal(matrix,index1,0)
        check_and_update(result_dict,str1,word_list)
        index1 -= 1
    index2 = 1
    while index2 < len(matrix[0]):
        str2 = right_diagonal(matrix,(len(matrix) - 1),index2)
        check_and_update(result_dict,str2,word_list)
        index2 += 1
    return result_dict


def right_diagonal(matrix,i,j):
    """
     Make string in direction - right diagonal up
     :param: matrix: a matrix to make the string from
     :param: i: index1
     :param: j: index2
     :return: the string
     """
    string = ''
    while i >= 0 and j < len(matrix[0]):
        string += matrix[i][j]
        i -= 1
        j += 1
    return string


def check_left_up(result_dict,word_list,matrix):
    """
     Check if words in the matrix in direction - left diagonal up
     :param: result_dict: a dict with the result of the word founds so far
     :param: word_list: a list of words
     :param: matrix: a matrix to check on
     :return: the updated dict
     """
    index1 = len(matrix) - 1
    while index1 >= 0:
        str1 = left_diagonal(matrix,index1,len(matrix[0]) - 1)
        check_and_update(result_dict,str1,word_list)
        index1 -= 1
    index2 = len(matrix[0]) - 2
    while index2 >= 0:
        str2 = left_diagonal(matrix,(len(matrix) - 1),index2)
        check_and_update(result_dict,str2,word_list)
        index2 -= 1
    return result_dict


def left_diagonal(matrix,i,j):
    """
     Make string in direction - left diagonal up
     :param: matrix: a matrix to make the string from
     :param: i: index1
     :param: j: index2
     :return: the string
     """
    string = ''
    while i >= 0 and j >= 0:
        string += matrix[i][j]
        i -= 1
        j -= 1
    return string


def check_right_down(result_dict,word_list,matrix):
    """
     Check if words in the matrix in direction - right diagonal down
     :param: result_dict: a dict with the result of the word founds so far
     :param: word_list: a list of words
     :param: matrix: a matrix to check on
     :return: the updated dict
     """
    index1 = 0
    while index1 < len(matrix):
        str1 = right_down_diagonal(matrix,index1,0)
        check_and_update(result_dict,str1,word_list)
        index1 += 1
    index2 = 1
    while index2 < len(matrix[0]):
        str2 = right_down_diagonal(matrix,0,index2)
        check_and_update(result_dict,str2,word_list)
        index2 += 1
    return result_dict


def right_down_diagonal(matrix,i,j):
    """
     Make string in direction - right diagonal down
     :param: matrix: a matrix to make the string from
     :param: i: index1
     :param: j: index2
     :return: the string
     """
    string = ''
    while i < len(matrix) and j < len(matrix[0]):
        string += matrix[i][j]
        i += 1
        j += 1
    return string


def check_left_down(result_dict,word_list,matrix):
    """
     Check if words in the matrix in direction - left diagonal down
     :param: result_dict: a dict with the result of the word founds so far
     :param: word_list: a list of words
     :param: matrix: a matrix to check on
     :return: the updated dict
     """
    index1 = 0
    while index1 < len(matrix):
        str1 = left_down_diagonal(matrix,index1,len(matrix[0]) - 1)
        check_and_update(result_dict,str1,word_list)
        index1 += 1
    index2 = len(matrix[0]) - 2
    while index2 >= 0:
        str2 = left_down_diagonal(matrix,0,index2)
        check_and_update(result_dict,str2,word_list)
        index2 -= 1
    return result_dict


def left_down_diagonal(matrix,i,j):
    """
     Make string in direction - left diagonal down
     :param: matrix: a matrix to make the string from
     :param: i: index1
     :param: j: index2
     :return: the string
     """
    string = ''
    while i < len(matrix) and j >= 0:
        string += matrix[i][j]
        i += 1
        j -= 1
    return string


def get_directions(word_list,matrix,directions):
    """
    Check if words in the matrix by the directions given
    and updated it into a result list
     :param: word_list: a list of words
     :param: matrix: a matrix to check on
     :return: result list
    """
    result_dict = dict()
    if 'u' in directions:
        check_up(result_dict,word_list,matrix)
    if 'd' in directions:
        check_down(result_dict,word_list,matrix)
    if 'r' in directions:
        check_right(result_dict,word_list,matrix)
    if 'l' in directions:
        check_left(result_dict,word_list,matrix)
    if 'w' in directions:
        check_right_up(result_dict,word_list,matrix)
    if 'x' in directions:
        check_left_up(result_dict,word_list,matrix)
    if 'y' in directions:
        check_right_down(result_dict,word_list,matrix)
    if 'z' in directions:
        check_left_down(result_dict,word_list,matrix)
    result_list = make_list_from_dict(word_list,result_dict)
    return result_list


def make_list_from_dict(word_list,result_dict):
    """
    Make a list of Tuples from the result dict
     :param: word_list: a list of words
     :param: result_dict: a dict to make a list from
     :return: result list
    """
    result_list = []
    for word in word_list:
        if word in result_dict:
            result_list.append((word,result_dict[word]))
    return result_list


def find_words(word_list,matrix,directions):
    """
    Search for words from word list in the matrix
    and count the appearance and updated it into a Tuples in result list
     :param: word_list: a list of words
     :param: matrix: a matrix to check on
     :param: directions: directions to search in the matrix
     :return: result list
    """
    result_list = get_directions(word_list,matrix,directions)
    return result_list


def main():
    """
     The main func, make it all works together.
     Checking if files exists and if its a valid input.
     Reads the files and search for words.
     Writing output to result file.
    """
    arguments = sys.argv
    if files_exists(arguments[1], arguments[2]) and \
            valid_input(arguments[4]) and correct_num_of_args(arguments):

        matrix = read_matrix(arguments[2])
        word_list = read_wordlist(arguments[1])
        result = find_words(word_list, matrix, arguments[4])
        write_output(result, arguments[3])


if __name__ == '__main__':
    main()
