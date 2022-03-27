############################################################
# FILE : car.py
# WRITER : Yair Shtern , yair.shtern , 318442241
# EXERCISE : intro2cs1 ex9 2020
# DESCRIPTION: Car class for Rush Hour
############################################################
VERTICAL = 0
HORIZONTAL = 1

DIRECTIONS = ['u', 'd', 'r', 'l']

class Car:
    """
    Class Car for Rush Hour board.
    """

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.__name = name
        self.__length = length
        self.__location = location
        self.__orientation = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        location = []
        if self.__orientation == VERTICAL:
            for i in range(self.__length):
                location.append((self.__location[0] + i, self.__location[1]))
        if self.__orientation == HORIZONTAL:
            for i in range(self.__length):
                location.append((self.__location[0], self.__location[1] + i))
        return location

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        moves = "There is no possible move"
        if self.__orientation == VERTICAL:
            moves = {'u': "move the car up",
                     'd': "move the car down"}
        if self.__orientation == HORIZONTAL:
            moves = {'r': "move the car to the right",
                     'l': "move the car to the left"}
        return moves

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        requirements = []
        front_row, front_col = self.__location
        back_row, back_col = self.__location
        if self.__orientation == VERTICAL:
            back_row, back_col = self.__location
            back_row += self.__length - 1
        if self.__orientation == HORIZONTAL:
            back_row, back_col = self.__location
            back_col += self.__length - 1
        if movekey == 'u':
            requirements = [(front_row - 1, front_col)]
        if movekey == 'l':
            requirements = [(front_row, front_col - 1)]
        if movekey == 'd':
            requirements = [(back_row + 1, back_col)]
        if movekey == 'r':
            requirements = [(back_row, back_col + 1)]
        return requirements

    def move(self, movekey):
        """
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        front = (self.__location[0], self.__location[1])
        if self.__orientation == VERTICAL:
            if movekey == 'u':
                self.__location = (front[0] - 1, front[1])
                return True
            if movekey == 'd':
                self.__location = (front[0] + 1, front[1])
                return True
        if self.__orientation == HORIZONTAL:
            if movekey == 'l':
                self.__location = (front[0], front[1] - 1)
                return True
            if movekey == 'r':
                self.__location = (front[0], front[1] + 1)
                return True
        return False

    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.__name