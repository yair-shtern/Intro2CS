#####################################################
# FILE : ex3.py
# WRITER : Yair Shtern
# EXERCISE : intro2cs1 ex3 2020
# DESCRIPTION: A program about loops and lists
#####################################################
def input_list():
    ''' A function that receives from the use a input of string of numbers
    and returns them within a list, the last index in the list is the sum
    of the numbers. The user must enter an empty string to stop'''
    user_string = input()
    user_list = list()
    sum_string = 0
    while user_string:
        user_string = float(user_string)
        user_list.append(user_string)
        sum_string += user_string
        user_string = input()
    user_list.append(sum_string)
    return user_list

def inner_product(vec_1, vec_2):
    ''' A function that gets two lists of numbers
    and returns list with the result of the inner product.'''
    if vec_1 == [] and vec_2 == []:
        return 0
    if vec_1 == [] or vec_2 == []:
        return None
    elif len(vec_1) != len(vec_2):
        return 0
    sum = 0
    for i in range(len(vec_1)):
        sum += float(vec_1[i])*float(vec_2[i])
    return sum


def sequence_monotonicity(sequence):
    ''' A function that gets two list of numbers
    and returns list of four indexes withe boolean value (True/False):
    The first index answers whether
    the index in position i <= from the index in position i+1.
    The second index answers whether
    the index in position i < from the index in position i+1.
    The third index answers whether
    the index in position i => from the index in position i+1.
    The fourth index answers whether
    the index in position i > from the index in position i+1.'''
    sequence_list = []
    chek_if_True1 = True
    chek_if_True2 = True
    chek_if_True3 = True
    chek_if_True4 = True
    if sequence != [] and len(sequence) != 1:
        for i in range(0,len(sequence)-1):
            if sequence[i] > sequence[i+1]:
                if chek_if_True1:
                    chek_if_True1 = False

            if sequence[i] >= sequence[i+1]:
                if chek_if_True2:
                    chek_if_True2 = False

            if sequence[i] < sequence[i+1]:
                if chek_if_True3:
                    chek_if_True3 = False

            if sequence[i] <= sequence[i+1]:
                if chek_if_True4:
                    chek_if_True4 = False

    sequence_list = [chek_if_True1, chek_if_True2,
                     chek_if_True3, chek_if_True4]
    return sequence_list


def monotonicity_inverse(def_bool):
    '''The opposite of the previous function.
    The function gets a 4 indexes list with a boolean value,
    that represent the monotonicity of a list
    and returns an example of a function that maintains these attributes'''
    if def_bool[1] == def_bool[3] == True:
        return None
    if def_bool[1] == def_bool[2] == True:
        return None
    if def_bool[0] == def_bool[3] == True:
        return None
    if def_bool[0] == def_bool[2] == True:
        return [1,1,1,1]

    if def_bool[0] == True and def_bool[2] == def_bool[3] == False:
        if def_bool[1]:
            return [1,2,3,4]
        else:
            return [1,2,2,3]
    if def_bool[2] == True and def_bool[0] == def_bool[1] == False:
        if def_bool[3]:
            return [4,3,2,1]
        else:
            return [3,2,2,1]
    if def_bool[0] == def_bool[1] == def_bool[2] == def_bool[3] == False:
        return [1,2,1,2]

    else:
        return None


def primes_for_asafi(n):
    '''The function returns a list with the first n Primes'''
    n_primes = []
    if n == 0:
        return n_primes
    n_primes.append(2)
    i = 2
    while len(n_primes) < n:
        i += 1
        x = 2
        for j in range(2,i):
            if i%j == 0:
                break
            x += 1
        if x == i:
            n_primes.append(i)
    return n_primes


def sum_of_vectors(vec_lst):
    '''The function gets a list that contains several lists of vectors
    and returns a list that represents the sum of the vectors'''
    if vec_lst == []:
        return None
    sum_lists = []
    if vec_lst[0] == []:
        return sum_lists
    for j in range(len(vec_lst[0])):
        i = 0
        sum = 0
        while i < len(vec_lst):
            sum += vec_lst[i][j]
            i += 1
        sum_lists.append(sum)
    return sum_lists


def num_of_orthogonal(vectors):
    '''The function gets a list that contains several lists of vectors
     and returns the number of lists that are orthogonal to each other'''
    sum = 0
    if vectors == []:
        return
    if len(vectors) == 1:
        return sum
    for i in range(len(vectors)):
        for j in range((i+1), len(vectors)):
            if inner_product(vectors[i],vectors[j]) == 0:
                sum +=1
    return sum