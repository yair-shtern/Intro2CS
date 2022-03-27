class Ship:
    """
    A class represents the ship object with the properties of,
    direction, position and speed it is.
    """

    def __init__(self, x_location, y_location, x_speed, y_speed, direction, lives):
        """
        Initial constructor for a ship object.
        :param x_location: A positive int Represents the location
         of the ship on the X-axis.
        :param y_location:A positive int Represents the location
         of the ship on the X-axis.
        :param x_speed:Represents the speed of the ship
        relative to the y-axis.
        :param y_speed:Represents the speed of the ship
        relative to the y-axis.
        :param direction:Represents the direction of the ship (in degrees) .
        :param lives: Represents the the ship life in the game.
        """
        self.__x_location = x_location
        self.__x_speed = x_speed
        self.__y_location = y_location
        self.__y_speed = y_speed
        self.__direction = direction  # (in degrees)
        self.__ship_lives = lives
        self.__ship_radius = 1

    def get_x_location(self):
        """
        :Returns: the location of the ship on the x-axis.
        """
        return self.__x_location

    def get_x_speed(self):
        """
        :Returns: the speed of the ship on the x-axis.
        """
        return self.__x_speed

    def get_y_location(self):
        """
        :Returns: the location of the ship on the y-axis.
        """
        return self.__y_location

    def get_y_speed(self):
        """
        :Returns: the speed of the ship on the y-axis.
        """
        return self.__y_speed

    def get_direction(self):
        """
        :Returns: the direction of the ship in degrees
        (0 is parallel to x-axis).
        """
        return self.__direction

    def get_ship_lives(self):
        """
        :return: the remaining life of the ship.
        """
        return self.__ship_lives

    def get_radius(self):
        """
        :returns: the ships radius of.
        """
        return self.__ship_radius

    def remove_life(self):
        """
        Remove 1 life from the ship lives.
        :return:
        """
        self.__ship_lives -= 1

    def set_x_location(self, new_location):
        """
        Initializes the location of the ship on the x-axis.
        :param new_location:The new  location of the ship on the x-axis.
        :return: None
        """
        self.__x_location = new_location

    def set_y_location(self, new_location):
        """
        Initializes the location of the ship on the y-axis.
        :param new_location:The new  location of the asteroid on the y-axis.
        """
        self.__y_location = new_location

    def set_x_speed(self, speed):
        """
        Initializes the speed of the ship on the x-axis.
        :param speed:The new speed of the ship on the x-axis.
        """
        self.__x_speed = speed

    def set_y_speed(self, speed):
        """
        Initializes the speed of the ship on the y-axis.
        :param speed:The new speed of the ship on the y-axis.
        """
        self.__y_speed = speed

    def set_direction(self, direction):
        """
        set a new direction of the ship by adding degrees
        to the current direction.
        :param direction:An integer represents degrees
        that is added to the current direction
        """
        self.__direction += direction
