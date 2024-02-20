# Exercise description

# The next step on our journey to create Wordle is to produce a program that 
# gives the player one shot at guessing the secret word. In this exercise, 
# you will prompt the user for a word that 5 letters long. If the word is not
# 5 letters, you will ask them to input another 5 letter word. Otherwise, you
# output a series of green/yellow/white squares corresponding to the input.

# We will use "logan" for the purposes of our example and testing. 

# ----------------------------------------------------------------------------

# Exmaple inputs and outputs

# What is your 5-letter guess? laggy
# 🟩🟨🟩🟨⬜
# Not quite. Play again soon!

# What is your 5-letter guess? began
# ⬜⬜🟩🟩🟩
# Not quite. Play again soon!

# What is your 5-letter guess? congradulations
# That was not 5 letters! Try again: python
# That was not 5 letters! Try again: lager
# 🟩🟨🟩⬜⬜
# Not quite. Play again soon!

# What is your 5-letter guess? logan
# 🟩🟩🟩🟩🟩
# Woo! You got it!

# ----------------------------------------------------------------------------

SECRET_WORD = "logan"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def wordle(SECRET_WORD):
    # Delete the word "pass" and write your code here
    pass

# ----------------------------------------------------------------------------
        
# These are unit tests that can be used to test your work
# Do NOT touch these for these exercises

import unittest
from unittest.mock import patch

class TestWordle(unittest.TestCase):
    def test_correct_guess(self):
        with patch('builtins.input', return_value=SECRET_WORD):
            with patch('builtins.print') as mock_print:
                wordle(SECRET_WORD)
        mock_print.assert_any_call(GREEN_BOX * 5)
        mock_print.assert_any_call("Woo! You got it!")

    def test_incorrect_guess(self):
        with patch('builtins.input', side_effect=["abcde", SECRET_WORD]):
            with patch('builtins.print') as mock_print:
                wordle(SECRET_WORD)
        mock_print.assert_any_call(WHITE_BOX * 5)
        mock_print.assert_any_call("Not quite. Play again soon!")

    def test_invalid_guess_length(self):
        with patch('builtins.input', side_effect=["abcd", "abcde", SECRET_WORD]):
            with patch('builtins.print') as mock_print:
                wordle(SECRET_WORD)
        mock_print.assert_any_call("That was not 5 letters! Try again:")
        mock_print.assert_any_call(WHITE_BOX * 5)
        mock_print.assert_any_call("Woo! You got it!")

if __name__ == '__main__':
    unittest.main()