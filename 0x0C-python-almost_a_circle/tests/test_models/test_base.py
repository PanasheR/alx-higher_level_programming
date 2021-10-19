#!/usr/bin/python3
"""
Unittest for Base class
"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_single_blankid(self):
        self.a0 = Base()
        self.assertEqual(self.a0.id, 1)

    def test_multiple_blankid(self):
        self.a0 = Base()
        self.a1 = Base(None)
        self.a2 = Base()
        self.assertEqual(self.a2.id, 3)

    def test_specific_id(self):
        self.d1 = Base()
        self.d2 = Base()
        self.d5 = Base(17)
        self.d3 = Base(90)
        self.assertEqual(self.d5.id, 17)

    def test_None_id(self):
        self.a1 = Base()
        self.a3 = Base(None)
        self.assertEqual(self.a3.id, 2)
