########################################################################
# FILE : nonogram.py
# WRITERS : Yair Shtern, David Zuravin
# EXERCISE : intro2cs1 ex10 2020
# DESCRIPTION: Asteroids Game
 ########################################################################
from screen import Screen
import sys
import random
import math
from ship import Ship
from asteroid import Asteroid
from torpedo import Torpedo

DEFAULT_VAL = 0
DEFAULT_ASTEROIDS_NUM = 5
ASTEROID_SPEED = [-4, -3, -2, -1, 1, 2, 3, 4]
DEFAULT_ASTEROID_SIZE = 3
DEFAULT_SHIP_LIVES = 3
ADD_POINTS = {1: 100, 2: 50, 3: 20}
ASTEROID_SPLIT = {2: 1, 3: 2}
MAX_TORPEDO_LIFE_TIME = 200
MAX_NUM_OF_TORPEDOES = 10


class GameRunner:
    """
    Initializes the game board with the required amount of asteroids.
    :param asteroids_amount:the required amount of asteroids.
    """

    def __init__(self, asteroids_amount):
        self.__screen = Screen()
        self.__score = DEFAULT_VAL
        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        x_ship = random.randint(self.__screen_min_x, self.__screen_max_x)
        y_ship = random.randint(self.__screen_min_y, self.__screen_max_y)
        self.__ship = Ship(x_ship, y_ship, DEFAULT_VAL, DEFAULT_VAL, DEFAULT_VAL, DEFAULT_SHIP_LIVES)
        self.__asteroids = []
        self._add_asteroids(asteroids_amount)
        self.__torpedoes = []
        self.__current_num_of_torpedoes = DEFAULT_VAL

    def _add_asteroids(self, asteroids_amount):
        """
        This function adds asteroids to the game at a random location
         of the board that move at a randomly set speed
        :param asteroids_amount:The amount of asteroids we would like to add.
        :return:None
        """
        i = 0
        while i < asteroids_amount:
            x_asteroid = random.randint(self.__screen_min_x, self.__screen_max_x)
            y_asteroid = random.randint(self.__screen_min_y, self.__screen_max_y)
            x_speed = random.choice(ASTEROID_SPEED)
            y_speed = random.choice(ASTEROID_SPEED)
            asteroid = Asteroid(x_asteroid, y_asteroid, x_speed, y_speed, DEFAULT_ASTEROID_SIZE)
            if asteroid.has_intersection(self.__ship):
                continue
            self.__asteroids.append(asteroid)
            self.__screen.register_asteroid(asteroid, DEFAULT_ASTEROID_SIZE)
            self.__screen.draw_asteroid(asteroid, x_asteroid, y_asteroid)
            i += 1

    def run(self):
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        # You should not to change this method!
        self._game_loop()
        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def move_object(self, object, old_x, old_y, speed_x, speed_y):
        """
        This function moves the objects on the board.
        :param object:ship or asteroid.
        :param old_x: The old location of the object on the X-axis.
        :param old_y: The old location of the object on the Y-axis.
        :param speed_x:The old speed of the object on the X-axis.
        :param speed_y:The old speed of the object on the Y-axis.
        :return:None
        """
        new_x = self.__screen_min_x + (
                (old_x + speed_x - self.__screen_min_x) % (self.__screen_max_x - self.__screen_min_x))
        new_y = self.__screen_min_y + (
                (old_y + speed_y - self.__screen_min_y) % (self.__screen_max_y - self.__screen_min_y))
        object.set_x_location(new_x)
        object.set_y_location(new_y)

    def spin_ship(self):
        """
        This function spins the ship left or right by 7 degrees,
        when the user presses right or left.
        :return:None
        """
        if self.__screen.is_right_pressed():
            self.__ship.set_direction(-7)
        if self.__screen.is_left_pressed():
            self.__ship.set_direction(7)

    def ship_acceleration(self):
        """
        This function accelerates the speed of the ship if the user clicks up.
        :return: None
        """
        if self.__screen.is_up_pressed():
            heading = math.radians(self.__ship.get_direction())  # * (math.pi / 180)
            new_speed_x = self.__ship.get_x_speed() + math.cos(heading)
            new_speed_y = self.__ship.get_y_speed() + math.sin(heading)
            self.__ship.set_x_speed(new_speed_x)
            self.__ship.set_y_speed(new_speed_y)

    def move_ship(self):
        """
        Responsible for moving the ship on board.
        :return:None
        """
        self.move_object(self.__ship, self.__ship.get_x_location(),
                         self.__ship.get_y_location(), self.__ship.get_x_speed(),
                         self.__ship.get_y_speed())

    def move_asteroids(self):
        """
        Responsible for the movement of the asteroids on the board
        :return: None
        """
        for asteroid in self.__asteroids:
            self.move_object(asteroid, asteroid.get_x_location(),
                             asteroid.get_y_location(), asteroid.get_x_speed(),
                             asteroid.get_y_speed())
            self.__screen.draw_asteroid(asteroid, asteroid.get_x_location(), asteroid.get_y_location())

    def ship_crash(self):
        """
        Responsible for informing the user in the event of a
        spacecraft collision with one of the asteroids,
        Remove one of the user's lives and removing the asteroid from the board.
        :return:None
        """
        for asteroid in self.__asteroids:
            if asteroid.has_intersection(self.__ship):
                self.__screen.show_message("Asteroid Crash",
                                           "The ship crashed on an asteroid")
                self.__ship.remove_life()
                self.__screen.remove_life()
                self.__screen.unregister_asteroid(asteroid)
                self.__asteroids.remove(asteroid)

    def torpedo_crash_an_asteroid(self):
        """
        Responsible in case of a torpedo hit one of the asteroids,
        add a score to the user and remove or split the asteroid
        (depending on the size of the asteroid).
        :return:None
        """
        for asteroid in self.__asteroids:
            for torpedo in self.__torpedoes:
                if asteroid.has_intersection(torpedo):
                    self.__score += ADD_POINTS[asteroid.get_size()]
                    self.__screen.set_score(self.__score)
                    self.__screen.unregister_torpedo(torpedo)
                    self.__torpedoes.remove(torpedo)
                    self.__current_num_of_torpedoes -= 1
                    if asteroid.get_size() != 1:
                        self.split_asteroid(asteroid, torpedo)

                    self.__screen.unregister_asteroid(asteroid)
                    self.__asteroids.remove(asteroid)

    def split_asteroid(self, asteroid, torpedo):
        """
        Responsible for splitting the asteroid into 2 smaller asteroids
        so that they move in opposite directions to each other.
        :param asteroid: A steroid-type object that we want to split.
        :param torpedo: An torpedo object.
        :return:None
        """
        x_speed = (torpedo.get_x_speed() + asteroid.get_x_speed()) / math.sqrt(
            math.pow(asteroid.get_x_speed(), 2) + math.pow(asteroid.get_y_speed(), 2))
        y_speed = (torpedo.get_y_speed() + asteroid.get_y_speed()) / math.sqrt(
            math.pow(asteroid.get_x_speed(), 2) + math.pow(asteroid.get_y_speed(), 2))
        size = ASTEROID_SPLIT[asteroid.get_size()]
        asteroid1 = Asteroid(asteroid.get_x_location(),
                             asteroid.get_y_location(), x_speed, y_speed, size)
        asteroid2 = Asteroid(asteroid.get_x_location(),
                             asteroid.get_y_location(), -x_speed, -y_speed, size)
        self.__screen.register_asteroid(asteroid1, size)
        self.__asteroids.append(asteroid1)
        self.__screen.register_asteroid(asteroid2, size)
        self.__asteroids.append(asteroid2)

    def shoot_torpedo(self):
        """
        The function allows the user to shoot torpedoes.
        :return: None
        """
        if self.__screen.is_space_pressed() and self.__current_num_of_torpedoes < MAX_NUM_OF_TORPEDOES:
            ship = self.__ship
            x_speed = ship.get_x_speed() + 2 * (math.cos(math.radians(ship.get_direction())))
            y_speed = ship.get_y_speed() + 2 * (math.sin(math.radians(ship.get_direction())))
            heading = math.radians(ship.get_direction())
            torpedo = Torpedo(ship.get_x_location(), ship.get_y_location(), x_speed, y_speed, heading)
            self.__torpedoes.append(torpedo)
            self.__screen.register_torpedo(torpedo)
            self.__current_num_of_torpedoes += 1

    def move_torpedoes(self):
        """
        Limits the amount of torpedoes that can be in the game at once,
        until one of the torpedoes collides with one of the asteroids,
        or runs out of life.
        :return:None
        """
        for torpedo in self.__torpedoes:
            if torpedo.get_life_time() == MAX_TORPEDO_LIFE_TIME:
                self.__screen.unregister_torpedo(torpedo)
                self.__torpedoes.remove(torpedo)
                self.__current_num_of_torpedoes -= 1
                continue

            self.move_object(torpedo, torpedo.get_x_location(),
                             torpedo.get_y_location(), torpedo.get_x_speed(), torpedo.get_y_speed())
            self.__screen.draw_torpedo(torpedo, torpedo.get_x_location(),
                                       torpedo.get_y_location(), torpedo.get_heading())
            torpedo.set_life_time()  # add 1 to the torpedo life time

    def check_if_game_over(self):
        """
        Check if the game should end
        :return: True if the game is over, otherwise return False
        """
        if self.__ship.get_ship_lives() == 0:
            self.__screen.show_message("Game Over", "The asteroids killed you!")
            return True

        if not self.__asteroids:
            self.__screen.show_message("You Won", "You defeated the galaxy!")
            return True

        if self.__screen.should_end():
            self.__screen.show_message("Good Bye", " We hope to see you soon")
            return True
        return False

    def _game_loop(self):
        """
        This function runs the game loop.
        :return:None
        """
        self.__screen.draw_ship(self.__ship.get_x_location(),
                                self.__ship.get_y_location(), self.__ship.get_direction())
        self.move_ship()
        self.spin_ship()
        self.ship_acceleration()
        self.shoot_torpedo()
        self.move_torpedoes()
        self.ship_crash()
        self.torpedo_crash_an_asteroid()
        self.move_asteroids()
        if self.check_if_game_over():
            self.__screen.end_game()
            sys.exit()


def main(amount):
    """
    The main function of the program that run the entire game.
    :param amount: amount of the required asteroid in the game.
    :return: None
    """
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
