import math


class Asteroid:
    """
     A class of an asteroid object with properties of size,
     speed of motion and position relative to the axes.
     """

    def __init__(self, x_location, y_location, x_speed, y_speed, size):
        """
        Initial constructor for an asteroid object.
        :param x_location: A positive int Represents the location
         of an object on the X-axis.
        :param y_location:A positive int Represents the location
         of an object on the X-axis.
        :param x_speed:Represents the speed of the asteroid
        relative to the y-axis.
        :param y_speed:Represents the speed of the asteroid
        relative to the y-axis.
        :param size:Represents the size of the asteroid .
        """
        self.__x_location = x_location
        self.__y_location = y_location
        self.__x_speed = x_speed
        self.__y_speed = y_speed
        self.__size = size
        self.__asteroid_radius = self.__size * 10 - 5

    def get_x_location(self):
        """
        :returns: the location of the asteroid on the x-axis.
        """
        return self.__x_location

    def get_x_speed(self):
        """
        :returns: the speed of the asteroid on the x-axis.
        """
        return self.__x_speed

    def get_y_location(self):
        """
        :returns: the location of the asteroid on the x-axis.
        """
        return self.__y_location

    def get_y_speed(self):
        """
        :returns: the speed of the asteroid on the y-axis.
        """
        return self.__y_speed

    def get_size(self):
        """
        :Returns: the direction of the asteroid.
        """
        return self.__size

    def get_radius(self):
        return self.__asteroid_radius

    def set_x_location(self, new_location):
        """
        Initializes the location of the asteroid on the X-axis.
        :param new_location:The new location of the asteroid on the X-axis.
        :return: None
        """
        self.__x_location = new_location

    def set_y_location(self, new_location):
        """
        Initializes the location of the asteroid on the y-axis.
        :param new_location: The new location of the asteroid on the y-axis.
        :return: None
        """
        self.__y_location = new_location

    def set_x_speed(self, speed):
        """Initializes the speed of the asteroid on the x-axis.
        :param speed:The new speed of the asteroid on the x-axis.
        :return: None
        """
        self.__x_speed = speed

    def set_y_speed(self, speed):
        """
        Initializes the speed of the asteroid on the y-axis.
        :param speed:The new speed of the asteroid on the y-axis.
        :return: None
        """
        self.__y_speed = speed

    def has_intersection(self, obj):
        distance = math.sqrt(math.pow(obj.get_x_location() - self.get_x_location(), 2) + math.pow(
            obj.get_y_location() - self.get_y_location(), 2))
        if distance <= self.get_radius() + obj.get_radius():
            return True
        return False
