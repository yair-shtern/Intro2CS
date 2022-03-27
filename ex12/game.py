########################################################################
# FILE : game.py
# WRITERS : Yair Shtern, David Zuravin
# EXERCISE : intro2cs1 ex12 2020
# DESCRIPTION: Boggle Game
########################################################################
import boggle_board_randomizer
import ex12_utils


class Game:
    def __init__(self, words):
        """
        initialize a single game
        :param words: dict of the game words
        """
        self.__board = boggle_board_randomizer.randomize_board()
        self.__words = words
        self.__score = 0
        self.__words_found = 0

    def play_turn(self, path):
        """
        plays a turn and checks if the word that represents by the path in the game words
        :param path:list of tuple represent the coordinate of the word.
        :return: True if the path is legal and the word was not already found
        """
        word = ex12_utils.is_valid_path(self.__board, path, self.__words)
        if word is None:
            return False
        if self.__words[word]:
            self.__words[word] = False
            self.__words_found += 1
            self.__score += len(word) ** 2
            return True
        return False

    def get_score(self):
        """
        get the score of the player for correct word.
        :return: int represent the score that player got.
        """
        return self.__score

    def num_words_found(self):
        """
        :return: the number of the correct words that player found.
        """
        return self.__words_found

    def get_val_at(self, row, col):
        """
        :return the value of the board in the given coordinate.
        :param row:represent row in the board.
        :param col: represent col in the board.
        :return: str on the dice in the given coordinate.
        """
        return self.__board[row][col]
