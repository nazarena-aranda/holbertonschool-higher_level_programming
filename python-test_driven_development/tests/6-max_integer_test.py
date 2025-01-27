#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_at_end(self):
        """Test when the max value is at the end of the list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test when the max value is at the beginning of the list"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test when the max value is in the middle of the list"""
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

    def test_one_negative_number(self):
        """Test a list with one negative number"""
        self.assertEqual(max_integer([-1, 2, 3, 4]), 4)

    def test_only_negative_numbers(self):
        """Test a list with only negative numbers"""
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_list_of_one_element(self):
        """Test a list with one element"""
        self.assertEqual(max_integer([42]), 42)

    def test_list_is_empty(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_list_with_floats(self):
        """Test a list with float numbers"""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

    def test_list_with_strings(self):
        """Test a list of strings"""
        self.assertEqual(max_integer(["a", "b", "c"]), "c")

    def test_invalid_inputs(self):
        """Test invalid inputs"""
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer("not a list")
