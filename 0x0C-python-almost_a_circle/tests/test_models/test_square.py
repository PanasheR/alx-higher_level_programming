#!/usr/bin/python3
"""
Unittest for Rectangle class
"""
import unittest

from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquare(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0
        open('Rectangle.json', 'w').close()
        open('Square.json', 'w').close()

    def test_sq_id1(self):
        self.a0 = Square(10, 3)
        self.a3 = Square(10, 2, 9, 12)
        self.assertEqual(self.a3.id, 12)

    def test_sq_str1(self):
        self.a0 = Square(1, 2)
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a0)
            self.assertEqual(f.getvalue(),'[Square] (1) 2/0 - 1\n')

    def test_sq_str2(self):
        self.a0 = Square(1, 2, 3)
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a0)
            self.assertEqual(f.getvalue(),'[Square] (1) 2/3 - 1\n')

    def test_sq_area(self):
        self.a0 = Square(91)
        self.assertEqual(self.a0.area(), 8281)

    def test_sq_noargs(self):
        try:
            self.a0 = Square()

        except:
            self.assertRaises(TypeError, "__init__() missing 1 required positional argument: 'size'")

    def test_sq_wrong_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Square("9")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r2 = Square(1, "8")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r3 = Square(1, 8, "9")

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r4 = Square(-9)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r5 = Square(0)

    def test_sq_wrong_size2(self):
        try:
            self.a0 = Rectangle(1, 2)
            self.a1 = Square(None)

        except:
            self.assertRaises(TypeError, "width must be an integer")

    def test_sq_wrong_size3(self):
        try:
            self.a0 = Rectangle(1, 2)
            self.a1 = Square([])

        except:
            self.assertRaises(TypeError, "width must be an integer")

    def test_sq_bad_size5(self):
        try:
            self.a0 = Square((1, 9))

        except:
            self.assertRaises(TypeError, "width must be an integer")

    def test_sq_bad_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            self.a0 = Square(1, -9, 1)

    def test_sq_bad_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            self.a0 = Square(1, 2, -9)

    def test_sq_str(self):
        self.a7 = Square(2, 2)
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a7)
            self.assertEqual(f.getvalue(),'[Square] (1) 2/0 - 2\n')

    def test_sq_dict(self):
        self.a0 = Square(2, 2)
        r1_dictionary = self.a0.to_dictionary()
        self.assertIs(type(r1_dictionary), dict)

    def test_sq_update1(self):
        self.a0 = Square(2, 2)
        self.a0.update()
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a0)
            self.assertEqual(f.getvalue(),'[Square] (1) 2/0 - 2\n')

    def test_sq_update2(self):
        self.a0 = Square(2, 2)
        self.a0.update(89)
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a0)
            self.assertEqual(f.getvalue(),'[Square] (89) 2/0 - 2\n')

    def test_sq_update3(self):
        self.a0 = Square(2, 2)
        self.a0.update(89, 1)
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a0)
            self.assertEqual(f.getvalue(), '[Square] (89) 2/0 - 1\n')

    def test_sq_update4(self):
        self.a0 = Square(2, 2)
        self.a0.update(89, 1, 2)
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a0)
            self.assertEqual(f.getvalue(),'[Square] (89) 2/0 - 1\n')

    def test_sq_update5(self):
        self.a0 = Square(2, 2)
        self.a0.update(89, 1, 2, 3)
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a0)
            self.assertEqual(f.getvalue(),'[Square] (89) 2/3 - 1\n')

    def test_sq_update7(self):
        self.a0 = Square(2, 2)
        self.a0.update(**{'id': 89})
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a0)
            self.assertEqual(f.getvalue(),'[Square] (89) 2/0 - 2\n')

    def test_sq_update8(self):
        self.a0 = Square(2, 2)
        self.a0.update(**{ 'id': 89, 'size': 1 })
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a0)
            self.assertEqual(f.getvalue(),'[Square] (89) 2/0 - 1\n')

    def test_sq_update9(self):
        self.a0 = Square(2, 2)
        self.a0.update(**{ 'id': 89, 'size': 1, 'x': 3 })
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a0)
            self.assertEqual(f.getvalue(),'[Square] (89) 3/0 - 1\n')

    def test_sq_update10(self):
        self.a0 = Square(2, 2)
        self.a0.update(**{ 'id': 89, 'size': 1, 'x': 3, 'y': 8})
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a0)
            self.assertEqual(f.getvalue(),'[Square] (89) 3/8 - 1\n')

    def test_sq_create1(self):
        self.a0 = Square(1, 0, 0, 89)
        self.a1 = Square.create(**{ 'id': 89 })
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a0)
            print(self.a1)
            print(self.a0 is self.a1)
            print(self.a0 == self.a1)
            self.assertEqual(f.getvalue(),"[Square] (89) 0/0 - 1\n[Square] (89) 0/0 - 1\nFalse\nFalse\n")

    def test_sq_create2(self):
        self.a0 = Square(1, 0, 0, 89)
        self.a1 = Square.create(**{ 'id': 89, 'size': 1})
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a0)
            print(self.a1)
            print(self.a0 is self.a1)
            print(self.a0 == self.a1)
            self.assertEqual(f.getvalue(),"[Square] (89) 0/0 - 1\n[Square] (89) 0/0 - 1\nFalse\nFalse\n")

    def test_sq_create3(self):
        self.a0 = Square(1, 2, 3, 89)
        self.a1 = Square.create(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3})
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a0)
            print(self.a1)
            print(self.a0 is self.a1)
            print(self.a0 == self.a1)
            self.assertEqual(f.getvalue(),"[Square] (89) 2/3 - 1\n[Square] (89) 2/3 - 1\nFalse\nFalse\n")

    def test_sq_save1(self):
        Square.save_to_file(None)
        with patch('sys.stdout', new=StringIO()) as f:
            with open("Square.json", "r") as file:
                print(file.read())
                self.assertEqual(f.getvalue(),"[]\n")

    def test_sq_save2(self):
        Square.save_to_file([])
        with patch('sys.stdout', new=StringIO()) as f:
            with open("Square.json", "r") as file:
                print(file.read())
                self.assertEqual(f.getvalue(),"[]\n")

    def test_sq_save3(self):
        r0 = Square(90, 2, 3, 7)

        Square.save_to_file([Square(90, 2, 3, 7)])
        f_dictionary_list = Square.load_from_file()
        f_dictionary2 = f_dictionary_list[0]

        output1 = StringIO()
        print(r0, file=output1, end='')
        contents1 = output1.getvalue()
        output1.close()

        output2 = StringIO()
        print(f_dictionary2, file=output2, end='')
        contents2 = output2.getvalue()
        output2.close()

        self.assertEqual(contents1, contents2)

    def test_sq_no_load(self):
        f_dictionary_list_b = Square.load_from_file()
        output = StringIO()
        print(f_dictionary_list_b, file=output, end='')
        contents = output.getvalue()
        output.close()
        self.assertEqual(contents, "[]")
