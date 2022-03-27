# READ THIS FILE ENTIRELY!!!
# Read the instructions(!!!)
# if a test has failed look at troubleshooting in the end of this file

# NOTE!
# This tests were written by a fellow student.
# They might have bugs
# They are 100% not covering every thing the official tests check
# They might test functionality which is different from what's instructed
# USE THEM AT YOUR OWN RISK AND JUDGMENT
# Best of luck <3


# Instructions:
# 1. Extract the content of the zip to your root directory
#     so the tests and the test_files folder are at the same level with
#     the ex7.py file
# 2. Install pytest (pip install pytest)
# 3. Install mypy (pip install mypy)
# 4. In the command line (terminal tab on pycharm) run "pytest"
#     Make sure you do so from the root directory
# 5. Pass all tests!

# Troubleshooting:
My tests failed, what does it mean?

------- test_main.py --------
test_check_exists_ex7_file:
    Either you have misspelled the name or your main file doesn't exist
test_function_names:
    You have misspelled one of the functions or it just doesn't exist
test_mypy:
    Checks your static typing

------- test_simple.py --------
test_print_to_n:
    Tests for 0
    The function digit_sum has failed or returned an unexpected value
    look at the tests output for further data

test_digit_sum:
    The function digit_sum has failed or returned an unexpected value
    look at the tests output for further data

test_is_prime:
    The function is_prime has failed or returned an unexpected value
    look at the tests output for further data

------- test_hanoi.py --------
test_hanoi:
    The test checks handling negative and zero inputs
    The test will fail if you perform an illegal action (Large disc on smaller disc)
    The test will fail if not all discs are in the right place eventually
    Also for any error in your code obviously


------- test_advanced.py --------
test_print_sequences:
    Tests for empty list
    Tests for n = 0
        "But I think you don't need to print anything!"
        That's fine, the instructions were unclear, I implemented the tests
        the way I understood the instructions

    Expected result files are at test_files/sequences
    Each result file name is "abcd_4" where abcd are the letters sent to the
    function and 4 is the combination length requested

test_print_no_repetition_sequences:
    Tests for empty list
    Tests for n = 0
    Tests for len(char_list) < n
    "But I think you don't need to print anything!"
        That's fine, the instructions were unclear, I implemented the tests
        the way I understood the instructions

    Expected result files are at test_files/no_repeats
    Each result file name is "abcd_4" where abcd are the letters sent to the
    function and 4 is the combination length requested

test_parentheses:
    Checks for n =0
    "But I think you should return an empty array!"
        That's fine, the instructions were unclear, I implemented the tests
        the way I understood the instructions

test_flood_fill:
    Just some tests on some optional outputs
    Cheers to Golan for the examples I took from his tests
