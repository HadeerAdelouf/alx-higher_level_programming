#!/usr/bin/python3

"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_Ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [4, 5, 6, 7]
        self.assertEqual(max_integer(ordered), 7)

    def test_unordered_list(self):
        unordered = [1, 2, 4, 0]
        self.assertEqual(max_integer(unordered), 4)

    def test_no_arg(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer(), None)

    def test_empty_list(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([8]), 8)

    def test_identical_elements(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_floats(self):
        """Test a list of floats."""
        floats = [3.93, 5.33, -2.13, 15.9, 7.0]
        self.assertEqual(max_integer(floats), 15.9)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [2.54, 17.5, -19, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 17.5)

    def test_positives_and_negatives(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer([-20, 44, 81, 24, -104, 99, 101, 210, -2516, -12]),
            210)

    def test_string1(self):
        """Test a string."""
        strinG = "hadeer"
        self.assertEqual(max_integer(strinG), 'r')

    def test_list_strings(self):
        """Test a list of strings."""
        stringS = ["hadeer", "is", "my", "name"]
        self.assertEqual(max_integer(stringS), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
