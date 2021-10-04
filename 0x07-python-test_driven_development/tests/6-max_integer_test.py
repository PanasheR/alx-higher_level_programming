#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_val(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer([11, 2, 3]), 11)
        self.assertEqual(max_integer([1, 21, 3]), 21)
        self.assertEqual(max_integer([1, 2, 7, 4]), 7)
        self.assertEqual(max_integer([1, 32, 3, 4]), 32)
        self.assertEqual(max_integer([1, -2, 3]), 3)
        self.assertEqual(max_integer([1, 2, 2]), 2)
