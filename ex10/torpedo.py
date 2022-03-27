class Torpedo:
    """
    A class of a torpedo object.
    """

    def __init__(self, x_location, y_location, x_speed, y_speed, heading):
        """
        Initial constructor for a torpedo object.
        :param x_location: A positive int Represents the location
        of an object on the X-axis.
        :param y_location:A positive int Represents the location
        of an object on the X-axis.
        :param x_speed:Represents the speed of the asteroid
        relative to the y-axis.
        :param y_speed:Represents the speed of the asteroid
        relative to the y-axis.
        :param heading: Represents the direction that the torpedo is heading.
        """
        self.__x_location = x_location
        self.__y_location = y_location
        self.__x_speed = x_speed
        self.__y_speed = y_speed
        self.__heading = heading
        self.__life_time = 0
        self.__torpedo_radius = 4

    def get_x_location(self):
        """
        :returns: the location of the torpedo on the x-axis.
        """
        return self.__x_location

    def get_x_speed(self):
        """
        :returns: the speed of the torpedo on the x-axis.
        """
        return self.__x_speed

    def get_y_location(self):
        """
        :returns: the location of the torpedo on the y-axis.
        """
        return self.__y_location

    def get_y_speed(self):
        """
        :returns: the speed of the torpedo on the y-axis.
        """
        return self.__y_speed

    def get_heading(self):
        """
        :returns: the direction that the torpedo is heading (in degrees).
        """
        return self.__heading

    def get_radius(self):
        """
        :returns: the radius that the torpedo is in.
        """
        return self.__torpedo_radius

    def get_life_time(self):
        """
        :returns: the life_time of the torpedo.
        """
        return self.__life_time

    def set_x_location(self, new_location):
        """
        Initializes the location of the torpedo on the x-axis.
        :param new_location: The new location of the torpedo on the x-axis.
        :return: None
        """
        self.__x_location = new_location

    def set_y_location(self, new_location):
        """
        Initializes the location of the torpedo on the y-axis.
        :param new_location: The new location of the torpedo on the y-axis.
        :return: None
        """
        self.__y_location = new_location

    def set_x_speed(self, speed):
        """
        Initializes the speed of the torpedo on the x-axis.
        :param speed:The new speed of the torpedo on the x-axis.
        :return: None
        """
        self.__x_speed = speed

    def set_y_speed(self, speed):
        """
        Initializes the speed of the torpedo on the y-axis.
        :param speed:The new speed of the torpedo on the y-axis.
        :return: None
        """
        self.__y_speed = speed

    def set_life_time(self):
        """
        Initializes the life_time of the torpedo.
        :return: None
        """
        self.__life_time += 1
