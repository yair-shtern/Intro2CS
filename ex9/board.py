############################################################
# FILE : board.py
# WRITER : Yair Shtern , yair.shtern , 318442241
# EXERCISE : intro2cs1 ex9 2020
# DESCRIPTION: Board class for Rush Hour
############################################################
EMPTY = '-'
TARGET = (3, 7)


class Board:
    """
    Class Board for Rush Hour board.
    """

    def __init__(self):
        board = [[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]]
        self.__board = board
        self.__cars = dict()

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        string = '* * * * * * * * * * * * *\n'
        for row in range(len(self.__board)):
            string += '* '
            for col in range(len(self.__board[row])):
                string += ' ' + self.__board[row][col] + ' '
            if row != 3:
                string += ' *' + '\n'
            else:
                string += '\n'
        string += '* * * * * * * * * * * * *\n'
        return string

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        lst = []
        for row in range(len(self.__board)):
            for col in range(len(self.__board[row])):
                lst.append((row, col))
        return lst

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description)
                 representing legal moves
        """
        moves = []
        for car in self.__cars:
            options = self.__cars[car].possible_moves()
            for move in options:
                legal_move = self.__cars[car].movement_requirements(move)
                row, col = legal_move[0]
                if (0 <= row <= 6 and 0 <= col <= 6 and self.__board[row][col] == EMPTY) or \
                        (row == 3 and col == 7 and self.__board[row][col] == EMPTY):
                    moves.append((car, move, options[move]))
        return moves

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        # In this board, returns (3,7)
        return TARGET

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        x, y = coordinate
        if self.__board[x][y] == EMPTY:
            return None
        return self.__board[x][y]

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        name = car.get_name()
        if name in self.__cars:
            return False
        lst = car.car_coordinates()
        for i in range(len(lst)):
            x, y = lst[i]
            if not (0 <= x <= 6 and 0 <= y <= 6) or self.__board[x][y] != EMPTY:
                return False
        for i in range(len(lst)):
            self.__board[lst[i][0]][lst[i][1]] = name
            self.__cars[name] = car
        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        if name not in self.__cars:
            return False
        requirements = self.__cars[name].movement_requirements(movekey)
        row, col = requirements[0]
        if (row == 3 and col == 7 and self.__board[row][col] == EMPTY) or \
                (0 <= row <= 6 and 0 <= col <= 6) and self.__board[row][col] == EMPTY:
            coordinates = self.__cars[name].car_coordinates()
            if self.__cars[name].move(movekey):
                self.__board[row][col] = name
                x, y = coordinates[0]
                if movekey == 'u' or movekey == 'l':
                    x, y = coordinates[-1]
                self.__board[x][y] = EMPTY
                return True
        return False
