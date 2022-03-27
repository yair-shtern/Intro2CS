########################################################################
# FILE : hangman.py
# WRITER : Yair Shtern , yair.shtern , 318442241
# EXERCISE : intro2cs1 ex4 2020
# DESCRIPTION: Hangman game
# The user need to guess a word hidden behind a pattern.
# For example the word 'abcd' will be displayed by the pattern '____'
#######################################################################
from hangman_helper import*
def update_word_pattern(word, pattern, letter):
    """
    Runs a single game until the user won or lost
    :param: word: the word that the pattern contains
        pattern: the current pattern
        letter: the chosen letter of the user
    :return: the update pattern
    """
    lst_new_pattern = []
    new_pattern = ''
    for i in range(len(word)):
        if letter == word[i]:
            lst_new_pattern.append(letter)
        else:
            lst_new_pattern.append(pattern[i])
    for i in range(len(lst_new_pattern)):
        new_pattern += str(lst_new_pattern[i])
    return new_pattern


def run_single_game(words_list, score):
    """
    Runs a single game until the user won or lost
    :param: words_list: a list of words
        score: the current point uf the user
    :return: the current score
    """
    word = get_random_word(words_list)
    current_pattern = '_'*len(word)
    correct_guesses = []
    wrong_guesses = []
    msg = "Let's play Hangman!"
    while score > 0 and word != current_pattern:
        display_state(current_pattern, wrong_guesses, score, msg)
        input = get_input()
        msg = 'Keep trying'
        if input[1] != None:
            if input[0] == LETTER:
                if len(input[1]) != 1 or input[1] in wrong_guesses or input[1] in correct_guesses \
                        or ord(input[1]) < 97 or ord(input[1]) > 122:
                    continue
                else:
                    score -=1
                    n = 0
                    for i in word:
                        if input[1] == i:
                            n += 1
                    if n > 0:
                        current_pattern = update_word_pattern(word, current_pattern, input[1])
                        score += (n*(n+1))//2
                        correct_guesses.append(input[1])
                    else:
                        wrong_guesses.append(input[1])
            elif input[0] == WORD:
                for j in input[1]:
                    if ord(j) < 97 or ord(j) > 122:
                        break
                score -= 1
                if input[1] == word:
                    s = 0
                    for i in range(len(word)):
                        if current_pattern[i] == '_':
                            s += 1
                    score += (s*(s+1))//2
                    current_pattern = word
        else:
            score -= 1
            hint = filter_words_list(words_list, current_pattern, wrong_guesses)
            length = len(hint)
            hint_list = []
            if length > HINT_LENGTH:
                x = 0
                while x < HINT_LENGTH:
                    hint_list.append(hint[length*x//HINT_LENGTH])
                    x += 1
            else:
                hint_list = hint
            show_suggestions(hint_list)
    if current_pattern == word:
        msg = 'Congratulations! you won! the hidden word is ' + word
    else:
        msg = 'Sorry you lost the hidden word is ' + word
    display_state(current_pattern, wrong_guesses, score, msg)
    return score

def filter_words_list(words, pattern, wrong_guess_lst):
    """
    Sets a 'hint' list of words that fits the pattern
    :param: words: a list of words
        pattern: the current pattern
        wrong_guess_lst: a list of wrong_guess_lst
    :return: a list of optional words
    """
    return_list = []
    for i in range(len(words)):
        if len(words[i]) != len(pattern):
            continue
        j = 0
        while j < len(pattern):
            if words[i][j] in wrong_guess_lst:
                break
            elif pattern[j] == '_':
                j += 1
                continue
            elif words[i][j] != pattern[j] or \
                    pattern.count(pattern[j]) != words[i].count(pattern[j]):
                j = 0
                break
            else:
                j+=1

        if j != 0:
            return_list.append(words[i])
    return return_list


def main():
    """
    Set the boards and starts the game
    :return: None
    """
    words = load_words()
    points = str(run_single_game(words , POINTS_INITIAL))
    msg = 'you played 1 game and you heve ' + points + ' points. Do you want to play again?'
    x = 1
    while play_again(msg):
        x = int(x)
        points = int(points)
        if points > 0:
            x += 1
            points = run_single_game(words, points)
        else:
            points = run_single_game(words, POINTS_INITIAL)
            x=1
        x = str(x)
        points = str(points)
        msg = 'you played ' + x + ' games and you heve ' + points + ' points. Do you want to play again?'

if __name__ == "__main__":
    main()

