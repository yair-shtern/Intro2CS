########################################################################
# FILE : boggle.py
# WRITERS : Yair Shtern, David Zuravin
# EXERCISE : intro2cs1 ex12 2020
# DESCRIPTION: Boggle Game (GUI)
########################################################################
import tkinter as tki
from ex12_utils import load_words_dict
from typing import Dict, List
from game import Game
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "violet", "gray"]
BOARD_SIZE = 4
REGULAR_COLOR = 'lightgray'
DICE_SELECTED_COLOR = 'lightblue'
DICE_STYLE = {"font": ("Courier", 30),
              "borderwidth": 1,
              "relief": tki.RAISED,
              "bg": REGULAR_COLOR,
              "activebackground": DICE_SELECTED_COLOR}
FRAME_STYLE = {"bg": REGULAR_COLOR, "highlightbackground": REGULAR_COLOR,
               "highlightthickness": 5}
LABELS_STYLE = {"font": ("Courier", 15), "bg": REGULAR_COLOR, "heigh": 2, "width": 10}
BUTTONS_STYLE = {"font": ("Courier", 10), "bg": REGULAR_COLOR, "heigh": 2, "width": 15}
MAX_CHARS_ON_DICE = 2
START_TIME = (2, 60)


class BoggleGUI:
    _dices: Dict[tuple, tki.Button] = {}
    _dices_chars: Dict[tuple, str] = {}
    _board: List[list]

    _words_found_label: tki.Label
    _play_again_label: tki.Label
    _start_button: tki.Button
    _quit_button: tki.Button
    _start_quit_button: tki.Button

    def __init__(self):
        """
        initialize the boggle game
        """
        self._root = tki.Tk()
        self._root.title("Boggle Game")
        self._root.resizable(False, False)
        self._words = load_words_dict("boggle_dict.txt")
        self._make_first_frame()

    def _make_first_frame(self):
        """
        Produces a starting frame with two buttons,
        one to exit the game and the other to start playing.
        :return:None
        """
        self._start_frame = tki.Frame(self._root, **FRAME_STYLE)
        self._start_frame.pack(side=tki.TOP, fill=tki.BOTH, expand=True)

        self._play_again_label = tki.Label(self._start_frame, text="LET'S PLAY BOGGLE", **LABELS_STYLE)
        self._play_again_label["heigh"] = 15
        self._play_again_label["width"] = 40
        self._play_again_label.pack(side=tki.TOP, fill=tki.BOTH)

        self._start_button = tki.Button(self._start_frame, text="LET'S PLAY", command=self._make_second_frame,
                                        **BUTTONS_STYLE)
        self._start_button.pack(side=tki.LEFT)

        self._quit_button = tki.Button(self._start_frame, text="QUIT", command=self._end_game, **BUTTONS_STYLE)
        self._quit_button.pack(side=tki.RIGHT)

    def _make_second_frame(self):
        """
        Replaces the initial frame with the frame of the game.
        :return:None
        """
        self._start_frame.destroy()

        self._make_game_frame()

    def _make_game_frame(self):
        """
        Produces the frame of the game.
        :return:None
        """
        self._make_display_frame()
        self._make_clock()
        self._make_board_frame()
        self._make_right_frame()
        self._create_start_quit_button()
        self._curr_time = START_TIME
        self._curr_path = []

    def _make_right_frame(self):
        """
        Produces the graphic part of the score in the frame of the game.
        :return:
        """
        self._right_frame = tki.Frame(self._root, **FRAME_STYLE)
        self._right_frame.pack(side=tki.LEFT, fill=tki.BOTH)
        self._score_title_label = tki.Label(self._right_frame, text="score", **LABELS_STYLE)
        self._score_title_label.pack(side=tki.TOP, fill=tki.Y)
        self._score_label = tki.Label(self._right_frame, relief="ridge", text=0, **LABELS_STYLE)
        self._score_label.pack(side=tki.TOP, fill=tki.Y)

    def _make_board_frame(self):
        """
        Produces the frame of the board in the frame of the game.
        :return:
        """
        self._board_frame = tki.Frame(self._root, **FRAME_STYLE)
        self._board_frame["bg"] = "white"
        self._board_frame.pack(side=tki.LEFT, fill=tki.BOTH, expand=True)

    def _make_clock(self):
        """
        Produces the graphic part of the clock in the frame of the game.
        :return:
        """
        self._clock_label = tki.Label(self._display_frame, relief="ridge", **LABELS_STYLE)
        self._clock_label.pack(side=tki.LEFT, fill=tki.Y)
        self._clock_label["font"] = ("blue", 15)
        self._clock_label["text"] = "3:00"

    def _make_display_frame(self):
        """
        Responsible for display the frame of the game.
        :return:
        """
        self._display_frame = tki.Frame(self._root, **FRAME_STYLE)
        self._display_frame.pack(side=tki.TOP, fill=tki.BOTH, expand=True)
        self._select_word_button = tki.Button(self._display_frame, text="select word", **BUTTONS_STYLE)
        self._select_word_button.pack(side=tki.LEFT, fill=tki.Y)
        self._select_word_button["command"] = self._check_word
        self._select_word_button["state"] = "disable"
        self._display_label = tki.Label(self._display_frame, relief="ridge", **LABELS_STYLE)
        self._display_label.pack(side=tki.LEFT, fill=tki.BOTH)
        self._display_label["width"] = 25
        self._display_label["text"] = "Let's Play Boggle"

    def set_display(self, display_text):
        self._display_label["text"] += display_text

    def get_display(self):
        return self._display_label["text"]

    def _create_start_quit_button(self):
        """
        Creates a start button that is also used to exit after the game has started.
        :return:
        """
        self._start_quit_button = tki.Button(self._right_frame, text="START",
                                             font=("Courier", 15), bg="lightgray", activebackground="red")
        self._start_quit_button.pack()
        self._start_quit_button["command"] = self._start_game

    def _start_game(self):
        """
        Starts the game when the user presses the button start.
        :return:
        """
        self._game = Game(self._words)
        self._make_words_list()
        self._run_clock()
        self._display_label["text"] = ""
        self._start_quit_button["text"] = "QUIT"
        self._score_label["text"] = self._game.get_score()
        self._start_quit_button["command"] = self._play_again
        self._select_word_button["state"] = "normal"
        self._make_board()

    def _make_board(self):
        """
        Produces a board for the game.
        :return:
        """
        for i in range(4):
            tki.Grid.columnconfigure(self._board_frame, i, weight=2)
        for i in range(4):
            tki.Grid.rowconfigure(self._board_frame, i, weight=2)
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                self._make_dice(col, row)

    def _make_dice(self, col, row):
        """
        Produces all the dice of the board.
        :param col:represent the col of the board.
        :param row:represent the row of the board.
        :return:None
        """
        char = self._game.get_val_at(row, col)
        dice = tki.Button(self._board_frame, text=char, **DICE_STYLE, background=random.choice(COLORS))
        if len(char) == MAX_CHARS_ON_DICE:
            dice["font"] = ("Courier", 20)
        dice.grid(row=row, column=col, sticky=tki.NSEW)
        self._dices_chars[(row, col)] = str(char)
        self._dices[(row, col)] = dice
        dice["command"] = lambda: self._do_dice_pressed(dice["text"], (row, col))

    def _make_words_list(self):
        """
        Responsible for the graphic part of the game that displays the words found.
        :return: None
        """
        self._words_found_label = tki.Label(self._right_frame, text="Words Found", font=("Courier", 15),
                                            bg=REGULAR_COLOR)
        self._words_box = tki.Listbox(self._right_frame, font=("Courier", 10))
        self._words_found_label.pack()
        self._words_box.pack()

    def _run_clock(self):
        """
        Starts the timer when the game starts.
        :return: None
        """
        if self._curr_time == (0, 0):
            self._play_again()
        else:
            self._clock_label["text"] = self._get_time_str()
            self._right_frame.after(1000, self._run_clock)

    def _get_time_str(self):
        """
        Responsible for the graphic representation of the clock on the board.
        :return: None
        """
        minute, seconds = self._curr_time
        if seconds == 0:
            minute -= 1
            seconds += 59
        else:
            seconds -= 1
        self._curr_time = (minute, seconds)
        if seconds < 10:
            seconds = '0' + str(seconds)
        return str(minute), ":", str(seconds)

    def _do_dice_pressed(self, dice_char, dice_coordinate):
        """
        If a cube is pressed the function is responsible for
        adding the dice to the path of the word
         and add the dice char to the label of the guss.
        :param dice_char: the char on the choosen dice.
        :param dice_coordinate: tuple of the dice coordinate on the board.
        :return:None
        """
        self._curr_path.append(dice_coordinate)
        self.set_display(dice_char)

    def _check_word(self):
        """
        check if the word guss is valid
        If so he puts it in the list of words found
        and add score to the player.
        :return:None
        """
        word = self.get_display()

        if self._game.play_turn(self._curr_path):
            self._words_box.insert(0, word)
            self._score_label["text"] = self._game.get_score()

        self._display_label["text"] = ""
        self._curr_path = []

    def _play_again(self):
        """
        When the game is over it clears the frame of the game
         and calls the function that produces the frame of.
        :return:None
        """
        self._clean_all()
        self._play_again_widgets()

    def _play_again_widgets(self):
        """
        Responsible for the graphic representation of the frame when the game
        is over The frame contains two buttons, exit and  new game
         and information on the amount score  of  the player and words found during the game.
        :return: None
        """
        self._play_again_frame = tki.Frame(self._root, **FRAME_STYLE)
        self._play_again_frame.pack(side=tki.TOP, fill=tki.BOTH, expand=True)

        self._play_again_label = tki.Label(self._play_again_frame, text="PLAY AGAIN", **LABELS_STYLE)
        self._play_again_label["heigh"] = 15
        self._play_again_label["width"] = 40
        message = "TIME IS UP!\nYOU HAVE FOUND " + str(self._game.num_words_found()) + " WORDS \nYOU SCORE " + str(
            self._game.get_score()) + " POINTS"
        self._play_again_label["text"] = message
        self._play_again_label.pack(side=tki.TOP, fill=tki.BOTH)

        self._start_button = tki.Button(self._play_again_frame, text="PLAY AGAIN", command=self._restart_game,
                                        **BUTTONS_STYLE)
        self._start_button.pack(side=tki.LEFT)

        self._quit_button = tki.Button(self._play_again_frame, text="QUIT", command=self._end_game, **BUTTONS_STYLE)
        self._quit_button.pack(side=tki.RIGHT)

    def _restart_game(self):
        """
        restart frame for a new game.
        :return: None
        """
        self._play_again_frame.destroy()
        self._make_game_frame()

    def _clean_all(self):
        """
        clean the frame of the game.
        :return: None
        """
        self._right_frame.destroy()
        self._board_frame.destroy()
        self._display_frame.destroy()

    def _end_game(self):
        """
        ends the game
        :return: None
        """
        self._root.quit()

    def run(self):
        """
        runs the game
        :return: None
        """
        self._root.mainloop()


if __name__ == '__main__':
    BoggleGUI().run()
