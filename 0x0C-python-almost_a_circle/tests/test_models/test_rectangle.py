#!/usr/bin/python3
"""
Unittest for Rectangle class
"""
import unittest
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0
        open('Rectangle.json', 'w').close()
        open('Square.json', 'w').close()

    def test_rect_id1(self):
        self.a0 = Rectangle(10, 3)
        self.a3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(self.a3.id, 12)

    def test_rect_area(self):
        self.a0 = Rectangle(7, 8, 9, 6)
        self.assertEqual(self.a0.area(), 56)

    def test_rect_noargs(self):
        try:
            self.a0 = Rectangle()

        except:
            self.assertRaises(TypeError, "__init__() missing 2 required positional arguments: 'width' and 'height'")

    def test_rect_one_arg(self):
        try:
            self.a9 = Rectangle(1)

        except:
            self.assertRaises(TypeError, "__init__() missing 1 required positional argument: 'height'")

    def test_rect_wrong_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle("2", 9)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r2 = Rectangle(2, "9")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r3 = Rectangle(2, 9, "99")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r4 = Rectangle(2, 9, 9, "99")

    def test_rect_wrong_height2(self):
        try:
            self.a0 = Rectangle(1, 2)
            self.a1 = Rectangle(2, None)

        except:
            self.assertRaises(TypeError, "height must be an integer")

    def test_rect_wrong_height3(self):
        try:
            self.a0 = Rectangle(1, 2)
            self.a1 = Rectangle(2, [])

        except:
            self.assertRaises(TypeError, "height must be an integer")

    def test_rect_bad_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.a1 = Rectangle(0, 9)

    def test_rect_bad_height(self):
         with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.a0 = Rectangle(1, -9)

    def test_rect_bad_height2(self):
         with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.a0 = Rectangle(1, 0)


    def test_rect_bad_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            self.a4 = Rectangle(1, 2, -9, 1)

    def test_rect_bad_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            self.a7 = Rectangle(1, 2, 9, -1)

    def test_rect_disp(self):
        self.a7 = Rectangle(2, 2)
        with patch('sys.stdout', new=StringIO()) as f:
            self.a7.display()
            self.assertEqual(f.getvalue(),'##\n##\n')

    def test_rect_disp2(self):
        self.a7 = Rectangle(2, 2, 1)
        with patch('sys.stdout', new=StringIO()) as f:
            self.a7.display()
            self.assertEqual(f.getvalue(),' ##\n ##\n')

    def test_rect_str(self):
        self.a7 = Rectangle(4, 6, 2, 1, 12)
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a7)
            self.assertEqual(f.getvalue(),'[Rectangle] (12) 2/1 - 4/6\n')

    def test_rect_dict(self):
        self.a0 = Rectangle(10, 2, 1, 9)
        r1_dictionary = self.a0.to_dictionary()
        self.assertIs(type(r1_dictionary), dict)

    def test_rect_update1(self):
        self.a0 = Rectangle(10, 10, 10, 10)
        self.a0.update()
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a0)
            self.assertEqual(f.getvalue(),'[Rectangle] (1) 10/10 - 10/10\n')

    def test_rect_update2(self):
        self.a0 = Rectangle(10, 10, 10, 10)
        self.a0.update(89)
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a0)
            self.assertEqual(f.getvalue(),'[Rectangle] (89) 10/10 - 10/10\n')

    def test_rect_update3(self):
        self.a0 = Rectangle(10, 10, 10, 10)
        self.a0.update(89, 1)
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a0)
            self.assertEqual(f.getvalue(),'[Rectangle] (89) 10/10 - 1/10\n')

    def test_rect_update4(self):
        self.a0 = Rectangle(10, 10, 10, 10)
        self.a0.update(89, 1, 2)
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a0)
            self.assertEqual(f.getvalue(),'[Rectangle] (89) 10/10 - 1/2\n')

    def test_rect_update5(self):
        self.a0 = Rectangle(10, 10, 10, 10)
        self.a0.update(89, 1, 2, 3)
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a0)
            self.assertEqual(f.getvalue(),'[Rectangle] (89) 3/10 - 1/2\n')

    def test_rect_update6(self):
        self.a0 = Rectangle(10, 10, 10, 10)
        self.a0.update(89, 1, 2, 3, 4)
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a0)
            self.assertEqual(f.getvalue(),'[Rectangle] (89) 3/4 - 1/2\n')

    def test_rect_update7(self):
        self.a0 = Rectangle(10, 10, 10, 10)
        self.a0.update(**{'id': 89})
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a0)
            self.assertEqual(f.getvalue(),'[Rectangle] (89) 10/10 - 10/10\n')

    def test_rect_update8(self):
        self.a0 = Rectangle(10, 10, 10, 10)
        self.a0.update(**{ 'id': 89, 'width': 1 })
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a0)
            self.assertEqual(f.getvalue(),'[Rectangle] (89) 10/10 - 1/10\n')

    def test_rect_update9(self):
        self.a0 = Rectangle(10, 10, 10, 10)
        self.a0.update(**{ 'id': 89, 'width': 1, 'height': 2 })
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a0)
            self.assertEqual(f.getvalue(),'[Rectangle] (89) 10/10 - 1/2\n')

    def test_rect_update10(self):
        self.a0 = Rectangle(10, 10, 10, 10)
        self.a0.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a0)
            self.assertEqual(f.getvalue(),'[Rectangle] (89) 3/10 - 1/2\n')

    def test_rect_update11(self):
        self.a0 = Rectangle(10, 10, 10, 10)
        self.a0.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a0)
            self.assertEqual(f.getvalue(),'[Rectangle] (89) 3/4 - 1/2\n')

    def test_rect_create1(self):
        self.a0 = Rectangle(1, 2, 0, 0, 89)
        self.a1 = Rectangle.create(**{ 'id': 89 })
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a0)
            print(self.a1)
            print(self.a0 is self.a1)
            print(self.a0 == self.a1)
            self.assertEqual(f.getvalue(),"[Rectangle] (89) 0/0 - 1/2\n[Rectangle] (89) 0/0 - 1/2\nFalse\nFalse\n")

    def test_rect_create2(self):
        self.a0 = Rectangle(1, 2, 0, 0, 89)
        self.a1 = Rectangle.create(**{ 'id': 89, 'width': 1 })
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a0)
            print(self.a1)
            print(self.a0 is self.a1)
            print(self.a0 == self.a1)
            self.assertEqual(f.getvalue(),"[Rectangle] (89) 0/0 - 1/2\n[Rectangle] (89) 0/0 - 1/2\nFalse\nFalse\n")

    def test_rect_create3(self):
        self.a0 = Rectangle(1, 2, 0, 0, 89)
        self.a1 = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2 })
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a0)
            print(self.a1)
            print(self.a0 is self.a1)
            print(self.a0 == self.a1)
            self.assertEqual(f.getvalue(),"[Rectangle] (89) 0/0 - 1/2\n[Rectangle] (89) 0/0 - 1/2\nFalse\nFalse\n")

    def test_rect_create4(self):
        self.a0 = Rectangle(1, 2, 0, 0, 89)
        self.a1 = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 7 })
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a0)
            print(self.a1)
            print(self.a0 is self.a1)
            print(self.a0 == self.a1)
            self.assertEqual(f.getvalue(),"[Rectangle] (89) 0/0 - 1/2\n[Rectangle] (89) 7/0 - 1/2\nFalse\nFalse\n")

    def test_rect_create5(self):
        self.a0 = Rectangle(1, 2, 0, 0, 89)
        self.a1 = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 7 })
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a0)
            print(self.a1)
            print(self.a0 is self.a1)
            print(self.a0 == self.a1)
            self.assertEqual(f.getvalue(),"[Rectangle] (89) 0/0 - 1/2\n[Rectangle] (89) 7/0 - 1/2\nFalse\nFalse\n")

    def test_rect_create6(self):
        self.a0 = Rectangle(1, 2, 0, 0, 89)
        self.a1 = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 7, 'y':4 })
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.a0)
            print(self.a1)
            print(self.a0 is self.a1)
            print(self.a0 == self.a1)
            self.assertEqual(f.getvalue(),"[Rectangle] (89) 0/0 - 1/2\n[Rectangle] (89) 7/4 - 1/2\nFalse\nFalse\n")

    def test_rect_save1(self):
        Rectangle.save_to_file(None)
        with patch('sys.stdout', new=StringIO()) as f:
            with open("Rectangle.json", "r") as file:
                print(file.read())
                self.assertEqual(f.getvalue(),"[]\n")

    def test_rect_save2(self):
        Rectangle.save_to_file([])
        with patch('sys.stdout', new=StringIO()) as f:
            with open("Rectangle.json", "r") as file:
                print(file.read())
                self.assertEqual(f.getvalue(),"[]\n")

    def test_rect_save3(self):
        r0 = Rectangle(1, 2, 3, 4, 5)

        Rectangle.save_to_file([Rectangle(1, 2, 3, 4, 5)])
        f_dictionary_list = Rectangle.load_from_file()
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

    def test_rect_no_load(self):
         f_dictionary_list = Rectangle.load_from_file()
         output1 = StringIO()
         print(f_dictionary_list, file=output1, end='')
         contents1 = output1.getvalue()
         output1.close()

         self.assertEqual(contents1, "[]")
