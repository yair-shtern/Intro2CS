########################################################################
# FILE : ex12_utils.py
# WRITERS : Yair Shtern, David Zuravin
# EXERCISE : intro2cs1 ex12 2020
# DESCRIPTION: Boggle Game - Functions
########################################################################
COORDINATES = [(1, 1), (-1, -1), (1, -1), (-1, 1),
               (0, 1), (0, -1), (1, 0), (-1, 0)]


def load_words_dict(file_path):
    """
    Produces a dictionary of all the words in the file so
    that each word has True value.
    :param file_path: file name
    :return: dictionary of words with a-True value.
    """
    with open(file_path) as names_file:
        names = dict()
        for line in names_file:
            word = line.strip('\n')
            names[word] = True
        return names


def is_valid_path(board, path, words):
    """
    The function checks if the path is a valid path
    that represents a word that exists in the dictionary.
    :param board:Representation of the game board.
    :param path:list of coordinates that represents a path in the board
    :param words:dictionary that the keys is words and all values is True
    :return:the word that the path represents, else return None.
    """
    if not path:
        return None

    for coordinate in path:
        x, y = coordinate
        if (not 0 <= x <= 3 or not 0 <= y <= 3) or \
                path.count(coordinate) != 1:
            return None

    x, y = path[0]
    word = board[x][y]
    for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]
        if (abs(x1 - x2) != 1 and x1 - x2 != 0) or \
                (abs(y1 - y2) != 1 and y1 - y2 != 0):
            return None
        word += board[x2][y2]
    if word in words:
        return word
    return None


def _find_path_for_word(board, word, curr_path, curr_coordinate, curr_word, path_for_word):
    """
    Returns a list of tuples that contain the word and its path.
    :param board:Representation of the game board.
    :param word: word to find path for in the board
    :param curr_path:list of coordinates of the current path to the current word
    :param curr_coordinate: coordinate of the last char of the current word
    :param curr_word: current word that in the board
    :param path_for_word: list of all paths for word in the board
    :return:Returns a list of tuples that contain the word and its path.
    """
    if curr_word not in word[:len(curr_word)]:
        return []
    if len(curr_word) == len(word):
        if curr_word == word:
            path_for_word.append((word, curr_path))
        return []

    x, y = curr_coordinate
    for add_x, add_y in COORDINATES:
        if 0 <= x + add_x <= 3 and 0 <= y + add_y <= 3 and \
                (x + add_x, y + add_y) not in curr_path and \
                word[len(curr_word)] in board[x + add_x][y + add_y]:
            _find_path_for_word(board, word, curr_path + [(x + add_x, y + add_y)],
                                (x + add_x, y + add_y), curr_word + board[x + add_x][y + add_y], path_for_word)

    return path_for_word


def _find_path(board, word):
    """
    find a-path for the word.
    :param board: Representation of the game board.
    :param word: word to check if is in the board.
    :return: list that contain path for the word.
    """
    path = []
    for row in range(len(board)):
        for col in range(len(board)):
            if word[0] in board[row][col] in word[0:]:
                path += _find_path_for_word(board, word, [(row, col)], (row, col), board[row][col], [])
    return path


def find_length_n_words(n, board, words):
    """
    The function returns a list of pairs Each pair is a tuple of words and tracks.
    The first organ in each pair is a string Which represents a word.
    The second limb is a list that describes the trajectory that fits that word.
    :param n: n a-natural number between 3 and 16.
    :param board:Representation of the game board.
    :param words:list of words in len n.
    return: list of tuples that represent the word and is path.
    """
    if n > 16 or n < 3:
        return []

    words_list = []
    for word in words:
        if len(word) == n:
            path = _find_path(board, word)
            if path:
                words_list += path
    return words_list
