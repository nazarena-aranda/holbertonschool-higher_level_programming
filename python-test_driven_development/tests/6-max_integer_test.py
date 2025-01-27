#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_none(self):
        self.assertEqual(max_integer([]), None)

    def test_uniq(self):
        self.assertEqual(max_integer([1]), 1)

    def test_same(self):
        self.assertEqual(max_integer([2, 2, 2]), 2)

    def test_middle(self):
        self.assertEqual(max_integer([1, 2, 1]), 2)

    def test_negative(self):
        self.assertEqual(max_integer([-3, -2, 0]), 0)

    def test_type(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, -100, "Hello"])

    def test_boolean(self):
        self.assertEqual(max_integer([2, True, False]), 2)

    def test_var_name(self):
        with self.assertRaises(NameError):
            max_integer([a, b])