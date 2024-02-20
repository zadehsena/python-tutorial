# In order to complete this you will need to know

# for-loops (https://www.w3schools.com/python/python_for_loops.asp)
# while-loops (https://www.w3schools.com/python/python_while_loops.asp)

# ----------------------------------------------------------------------------

# Exercise description

# Before we get back to building Wordle, we need to gain a basic understanding
# of loops. In this exercise you will write 5 different functions using either
# for-loops or while-loops to loop through a list and return the desired output.

# YOU HAVE TO USE A LOOP. No cheating using built in methods and functions.

# ----------------------------------------------------------------------------

# Given a list, write a function that sums all the values in the list.
# Return the sum (total) of all the values in the list.

# Examples
# [2,2] -> 4
# [1,2,3] -> 6
# [] -> 0

def sumValues(values):
    # Delete the word "pass" and write your code here
    pass

# Given a list, write a function to see if all the values in the a list are the same. 
# If they are all the same return True, else return False.
# Note: The list will be guaranteed to be len >= 1.

# Examples
# [2,2] -> True
# [1,2,3] -> False
# [1, None, 1] -> False

def sameValues(values):
    # Delete the word "pass" and write your code here
    pass

# Given a list, write a fucntion that finds the largest value in the list.
# Return the largest value in the list.
# Note: The list will be guaranteed to be len >= 1.

# Examples
# [1,2,3,4,5] -> 5
# [4,4,3,1,2]-> 4
# [0] -> 0

def largestValue(values):
    # Delete the word "pass" and write your code here
    pass

# Given a list, write a function that finds the second largest value in the list.
# Return the second largest value in the list.
# Note: The list will be guaranteed to be len >= 2.

# Examples
# [1,2,3,4,5] -> 4
# [4,4,3,1,2]-> 4
# [0,2] -> 0

def secondLargestValue(values):
    # Delete the word "pass" and write your code here
    pass

# Given a list, wite a function to calculate the average of the list.
# Return the average value of the list.
# Note: the list will be guaranteed to be len >= 1.

# Examples
# [1,2,3,4,5] -> 3
# [4,4,3,1,2]-> 2.8
# [0,2] -> 0

def averageValue(values):
    # Delete the word "pass" and write your code here
    pass

# ----------------------------------------------------------------------------
        
# These are unit tests that can be used to test your work
# Do NOT touch these for these exercises

import unittest

class Tests(unittest.TestCase):

    # sameValues tests
    def test_single_element_list(self):
        self.assertTrue(sameValues([5]))
    def test_all_same_positive_numbers(self):
        self.assertTrue(sameValues([7, 7, 7, 7, 7]))
    def test_all_same_negative_numbers(self):
        self.assertTrue(sameValues([-3, -3, -3, -3]))
    def test_not_all_same_mixed_numbers(self):
        self.assertFalse(sameValues([1, 2, 3, 4, 5]))
    def test_not_all_same_duplicate_values(self):
        self.assertFalse(sameValues([3, 8, 5, 8, 2]))

    # sumValues tests
    def test_single_element_list(self):
        self.assertEqual(sumValues([5]), 5)
    def test_positive_numbers(self):
        self.assertEqual(sumValues([1, 7, 3, 9, 2]), 22)
    def test_negative_numbers(self):
        self.assertEqual(sumValues([-5, -1, -8, -3]), -17)
    def test_mixed_numbers(self):
        self.assertEqual(sumValues([10, -4, 7, 0, -2]), 11)
    def test_duplicate_values(self):
        self.assertEqual(sumValues([3, 8, 5, 8, 2]), 26)

    # largestValue tests
    def test_single_element_list(self):
        self.assertEqual(largestValue([5]), 5)
    def test_positive_numbers(self):
        self.assertEqual(largestValue([1, 7, 3, 9, 2]), 9)
    def test_negative_numbers(self):
        self.assertEqual(largestValue([-5, -1, -8, -3]), -1)
    def test_mixed_numbers(self):
        self.assertEqual(largestValue([10, -4, 7, 0, -2]), 10)
    def test_duplicate_largest_value(self):
        self.assertEqual(largestValue([3, 8, 5, 8, 2]), 8)

    # secondLargestValue tests
    def test_two_element_list(self):
        self.assertEqual(secondLargestValue([5, 3]), 3)
    def test_positive_numbers(self):
        self.assertEqual(secondLargestValue([1, 7, 3, 9, 2]), 7)
    def test_negative_numbers(self):
        self.assertEqual(secondLargestValue([-5, -1, -8, -3]), -3)
    def test_mixed_numbers(self):
        self.assertEqual(secondLargestValue([10, -4, 7, 0, -2]), 7)
    def test_duplicate_largest_value(self):
        self.assertEqual(secondLargestValue([3, 8, 5, 8, 2]), 8)

    # averageValue tests
    def test_single_element_list(self):
        self.assertEqual(averageValue([5]), 5.0)
    def test_positive_numbers(self):
        self.assertAlmostEqual(averageValue([1, 7, 3, 9, 2]), 4.4, places=1)
    def test_negative_numbers(self):
        self.assertAlmostEqual(averageValue([-5, -1, -8, -3]), -4.25, places=2)
    def test_mixed_numbers(self):
        self.assertAlmostEqual(averageValue([10, -4, 7, 0, -2]), 2.2, places=1)
    def test_duplicate_values(self):
        self.assertAlmostEqual(averageValue([3, 8, 5, 8, 2]), 5.2, places=1)

if __name__ == '__main__':
    unittest.main()