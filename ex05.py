# In order to complete this you will need to know

# Python List Methods (https://www.w3schools.com/python/python_ref_list.asp)

# ----------------------------------------------------------------------------

# Exercise description

# You just studied all of the built-in list methods on w3school. Now I want
# you to implement them all from scratch without using the method itself.

# There are 11 function boilerplates below and I want to see how many you can 
# implement in one hour (most can be written in a single lin of code).

# After every function you write you can test the results by runinng this file. 
# There are multiple unit tests written for each function below.

# ----------------------------------------------------------------------------

# append() - Adds an element at the end of the list
# Example: [1,2,3], 4 → [1,2,3,4]
# Return orginal list with appended element

def manual_append(list, element):
    pass

# clear() - Removes all the elements from the list
# Example: [1,2,3] → []
# Return orginal list cleared

def manual_clear(lst):
    pass

# copy() - Returns a copy of the list
# Example: [1,2,3] → [1,2,3]
# Return a copy of the orginal list

def manual_copy(lst):
    pass

# count() - Returns the number of elements with the specified value
# Example: [1,2,3], 1 → 1
# Return number of times the value occurs in the list

def manual_count(lst, value):
    pass

# extend() - Add the elements of a list, to the end of the current list
# Example: [1,2,3], [4,5,6] → [1,2,3,4,5,6]
# Return a list with the vales of lst1 followed by values of lst2

def manual_extend(lst1, lst2):
    pass

# index() - Returns the index of the first element with the specified value
# Example: [1,2,3], 2 → 1
# Return the list index where the value first occurs

def manual_index(lst, value):
    pass

# insert() - Adds an element at the specified position
# Example: [1,2,4], 3, 2 → [1,2,3,4]
# Return the original list with the inserted element at the specified index

def manual_insert(lst, position, element):
    pass

# pop() - Removes the element at the specified position
# Example: [1,2,3], 1 → [1,3]
# Return the original list with the removed value at the specified index

def manual_pop(lst, position):
    pass

# remove () - Removes the first item with the specified value
# Example: [1,2,1], 1 → [2,1]
# Return the original list with the first item with the specified value removed 

def manual_remove(lst, value):
    pass

# reverse() - Reverses the order of the list
# Example: [1,2,3] → [3,2,1]
# Return the original list with values reversed

def manual_reverse(lst):
    pass

# sort() - Sorts the list
# Example: [3,1,2] → [1,2,3]
# Return the original list with values sorted

def manual_sort(lst):
    pass

# ----------------------------------------------------------------------------
        
# These are unit tests that can be used to test your work
# Do NOT touch these for these exercises

import unittest

class TestListMethods(unittest.TestCase):

    # append test cases
    if manual_append([], None) != None:

        def test_manual_append(self):
            lst = [1, 2, 3, 4]
            result = manual_append(lst, 5)
            self.assertEqual(result, [1, 2, 3, 2, 5])

        def test_manual_append_empty_list(self):
            lst = []
            result = manual_append(lst, 1)
            self.assertEqual(result, [1])

    # clear test cases
    if manual_clear([]) != None:

        def test_manual_clear_empty_list(self):
            lst = []
            result = manual_clear(lst)
            self.assertIsNone(result)
            self.assertEqual(lst, [])

        def test_manual_clear_non_empty_list(self):
            lst = [1, 2, 3, 4, 5]
            result = manual_clear(lst)
            self.assertIsNone(result)
            self.assertEqual(lst, [])
    
    # copy test cases
    if manual_clear([]) != None:

        def test_manual_copy_empty_list(self):
            lst = []
            copied_lst = manual_copy(lst)
            self.assertEqual(copied_lst, [])

        def test_manual_copy_non_empty_list(self):
            lst = [1, 2, 3, 4, 5]
            copied_lst = manual_copy(lst)
            self.assertEqual(copied_lst, lst)
            self.assertIsNot(copied_lst, lst)

    # count test cases
    if manual_clear([]) != None:

        def test_manual_count_empty_list(self):
            lst = []
            result = manual_count(lst, 5)
            self.assertEqual(result, 0)

        def test_manual_count_non_empty_list(self):
            lst = [1, 2, 3, 4, 5, 5, 5]
            result = manual_count(lst, 5)
            self.assertEqual(result, 3)

        def test_manual_count_non_existing_value(self):
            lst = [1, 2, 3, 4, 5]
            result = manual_count(lst, 6)
            self.assertEqual(result, 0)

        def test_manual_extend_empty_lists(self):
            lst1 = []
            lst2 = []
            manual_extend(lst1, lst2)
            self.assertEqual(lst1, [])

    # extend test cases
    if manual_extend([], []) != None:

        def test_manual_extend_non_empty_lists(self):
            lst1 = [1, 2, 3]
            lst2 = [4, 5, 6]
            manual_extend(lst1, lst2)
            self.assertEqual(lst1, [1, 2, 3, 4, 5, 6])

        def test_manual_extend_with_empty_list(self):
            lst1 = [1, 2, 3]
            lst2 = []
            manual_extend(lst1, lst2)
            self.assertEqual(lst1, [1, 2, 3])

        def test_manual_extend_empty_first_list(self):
            lst1 = []
            lst2 = [4, 5, 6]
            manual_extend(lst1, lst2)
            self.assertEqual(lst1, [4, 5, 6])

    # index test case
    if manual_index([], 0) != None:

        def test_manual_index_existing_value(self):
            lst = [1, 2, 3, 4, 5]
            result = manual_index(lst, 3)
            self.assertEqual(result, 2)

        def test_manual_index_non_existing_value(self):
            lst = [1, 2, 3, 4, 5]
            with self.assertRaises(ValueError):
                manual_index(lst, 6)

        def test_manual_index_duplicate_value(self):
            lst = [1, 2, 3, 3, 4, 5]
            result = manual_index(lst, 3)
            self.assertEqual(result, 2)

    # insert test cases
    if manual_insert([], 0, 0) != None:

        def test_manual_insert_in_middle(self):
            lst = [1, 2, 3, 4, 5]
            manual_insert(lst, 10, 2)
            self.assertEqual(lst, [1, 2, 10, 3, 4, 5])

        def test_manual_insert_at_beginning(self):
            lst = [1, 2, 3, 4, 5]
            manual_insert(lst, 10, 0)
            self.assertEqual(lst, [10, 1, 2, 3, 4, 5])

        def test_manual_insert_at_end(self):
            lst = [1, 2, 3, 4, 5]
            manual_insert(lst, 10, 5)
            self.assertEqual(lst, [1, 2, 3, 4, 5, 10])

    # pop test cases
    if manual_pop([], 0) != None:

        def test_manual_pop_from_middle(self):
            lst = [1, 2, 3, 4, 5]
            result = manual_pop(lst, 2)
            self.assertEqual(result, 3)
            self.assertEqual(lst, [1, 2, 4, 5])

        def test_manual_pop_from_beginning(self):
            lst = [1, 2, 3, 4, 5]
            result = manual_pop(lst, 0)
            self.assertEqual(result, 1)
            self.assertEqual(lst, [2, 3, 4, 5])

        def test_manual_pop_from_end(self):
            lst = [1, 2, 3, 4, 5]
            result = manual_pop(lst, 4)
            self.assertEqual(result, 5)
            self.assertEqual(lst, [1, 2, 3, 4])

    # remove test cases
    if manual_pop([], 0) != None:

        def test_manual_remove_existing_value(self):
            lst = [1, 2, 3, 4, 5]
            manual_remove(lst, 3)
            self.assertEqual(lst, [1, 2, 4, 5])

        def test_manual_remove_non_existing_value(self):
            lst = [1, 2, 3, 4, 5]
            with self.assertRaises(ValueError):
                manual_remove(lst, 6)

        def test_manual_remove_duplicate_value(self):
            lst = [1, 2, 3, 3, 4, 5]
            manual_remove(lst, 3)
            self.assertEqual(lst, [1, 2, 3, 4, 5])

    # sort test cases
    if manual_reverse([]) != None:

        def test_manual_reverse_even_length(self):
            lst = [1, 2, 3, 4]
            result = manual_reverse(lst)
            self.assertEqual(result, [4, 3, 2, 1])

        def test_manual_reverse_odd_length(self):
            lst = [1, 2, 3, 4, 5]
            result = manual_reverse(lst)
            self.assertEqual(result, [5, 4, 3, 2, 1])

        def test_manual_reverse_empty_list(self):
            lst = []
            result = manual_reverse(lst)
            self.assertEqual(result, [])

    # sort test cases
    if manual_sort([]) != None:

        def test_manual_sort(self):
            lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
            result = manual_sort(lst)
            self.assertEqual(result, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

        def test_manual_sort_empty_list(self):
            lst = []
            result = manual_sort(lst)
            self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()