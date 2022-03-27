############################################################
# FILE : game.py
# WRITER : Yair Shtern , yair.shtern , 318442241
# EXERCISE : intro2cs1 ex9 2020
# DESCRIPTION: Rush Hour
############################################################
def valid_input(user_input, legal_moves):
    """
    This function checks if the user input is valid
    :param user_input: the user input
    :param legal_moves:
    :return:
    """
    if len(user_input) != 3 or \
            user_input[1] != ',':
        return False
    for move in legal_moves:
        if user_input[0] == move[0]:
            if user_input[2] == move[1]:
                return True
    return False


class Game:
    """
    Class for Rush Hour game.
    The goal is to get one of the cars off the board
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.__board = board

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it.
        """
        pass

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        user_input = ''
        while user_input != '!':
            if self.__board.cell_content((3, 7)) is not None:
                break
            user_input = input('Enter the name of the car and'
                               ' the direction that you wont to move.')
            if user_input == '!':
                break
            legal_moves = self.__board.possible_moves()
            if not valid_input(user_input, legal_moves):
                print('Bad move. Try something else.')
                continue
            self.__board.move_car(user_input[0], user_input[2])
            print(self.__board)


if __name__ == "__main__":
    import helper
    import sys
    from car import *
    from board import *

    NAMES = ['Y', 'B', 'O', 'W', 'G', 'R']

    my_board = Board()  # restart the board
    cars = helper.load_json(sys.argv[1])  # read from Json file and add cars to the board
    for car1 in cars:
        if car1 in NAMES and (cars[car1][2] == 1 or cars[car1][2] == 0) and \
                (cars[car1][0] == 2 or cars[car1][0] == 3 or cars[car1][0] == 4):
            x, y = cars[car1][1]
            car1 = Car(car1, cars[car1][0], (x, y), cars[car1][2])
            my_board.add_car(car1)
    game = Game(my_board)
    print(my_board)
    game.play()
