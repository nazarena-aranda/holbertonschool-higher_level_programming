#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([10, 20, 30]), 30)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -5, -20]), -5)

    def test_mixed_integers(self):
        self.assertEqual(max_integer([-1, 0, 1, 2]), 2)
        self.assertEqual(max_integer([-10, 10, -20, 20]), 20)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([42]), 42)

    def test_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)

    def test_strings(self):
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer("not a list")
