# In order to complete this you will need to know

# print (https://www.w3schools.com/python/ref_func_print.asp)
# strings (https://www.w3schools.com/python/python_strings.asp)
# user input (https://www.w3schools.com/python/python_user_input.asp)
# if-else statements (https://www.w3schools.com/python/python_conditions.asp)

# ----------------------------------------------------------------------------

# Exercise description

# You will want to ask the user to enter a 5-character word and a single 
# character, storing both variables. You will then print out a diagnostic
# message, built-up using string concatenations. Then check each 
# index of the word string to see if it matches the character input.

# ----------------------------------------------------------------------------

# Exmaple inputs and outputs

# Enter a 5-character word: hello
# Enter a single character: e
# Searching for e in hello
# e found at index 1

# Enter a 5-character word: hello
# Enter a single character: l
# Searching for l in hello
# l found at index 2
# l found at index 3

# Enter a 5-character word: hello
# Enter a single character: o
# Searching for o in hello
# o found at index 4

# Enter a 5-character word: hello
# Enter a single character: d
# Searching for d in hello
# No instances of d found in hello


# Fail cases

# Enter a 5-character word: help
# Error: Word must contain 5 characters

# Enter a 5-character word: hello
# Enter a single character: world
# Error: Character must be a single character

# ----------------------------------------------------------------------------

# This is the function you will be writing
def wordle():
    # Delete the word "pass" and write you code here
    pass

# ----------------------------------------------------------------------------
        
# These are unit tests that can be used to test your work
# Do NOT touch these for these exercises

import unittest
from unittest.mock import patch
from io import StringIO

class TestWordleFunction(unittest.TestCase):

    @patch('builtins.input', side_effect=["hello", "h"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_valid_input(self, mock_stdout, mock_input):
        wordle()
        expected_output = "Searching for h in hello\nh found at index 0\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=["apple", "p"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_valid_input(self, mock_stdout, mock_input):
        wordle()
        expected_output = "Searching for p in apple\np found at index 1\np found at index 2\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=["tests", "k"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_valid_input(self, mock_stdout, mock_input):
        wordle()
        expected_output = "No instances of d found in hello\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=["python", "p"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_valid_input(self, mock_stdout, mock_input):
        wordle()
        expected_output = "Error: Word must contain 5 characters\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=["water", "can"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_valid_input(self, mock_stdout, mock_input):
        wordle()
        expected_output = "Error: Character must be a single character\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)
    
if __name__ == '__main__':
    unittest.main()