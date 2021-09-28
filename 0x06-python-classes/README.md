![spongebob with em weird sayings](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/247/oop-meme.jpg)

# 0x06. Python - Classes and Objects

https://python.swaroopch.com/oop.html (Read everything until the paragraph “Inheritance” excluded. You do NOT have to learn about class attributes, classmethod and staticmethod yet)

https://www.python-course.eu/python3_object_oriented_programming.php  (Please *be careful*: in most of the following paragraphs, the author shows things the way you should not use or write a class in order to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON’T have to learn about class attributes), Methods, The __init__ Method, “Data Abstraction, Data Encapsulation, and Information Hiding,” “Public, Protected, and Private Attributes”)

https://www.python-course.eu/python3_properties.php Properties vs. Getters and Setters

https://www.youtube.com/watch?v=1AGyBuVCTeE& Learn to Program 9 : Object Oriented Programming

https://www.youtube.com/watch?v=apACNr7DC_s Python Classes and Objects || Python Tutorial || Learn Python Programming

https://alx-intranet.hbtn.io/rltoken/-vVnWzwR3a3X0H8Oia78Ug 

Requirements

- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

#0 Write an empty class Square that defines a square:

    You are not allowed to import any module
    
#1 Write a class Square that defines a square by: (based on 0-square.py)

    Private instance attribute: size
    Instantiation with size (no type/value verification)
    You are not allowed to import any module
    Why?

    Why size is private attribute?

    The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute.     One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.
    
#2 Write a class Square that defines a square by: (based on 1-square.py)

    Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0):
    size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
    if size is less than 0, raise a ValueError exception with the message size must be >= 0
    You are not allowed to import any module
    
#3 Write a class Square that defines a square by: (based on 2-square.py)

    Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0):
    size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
    if size is less than 0, raise a ValueError exception with the message size must be >= 0
    Public instance method: def area(self): that returns the current square area
    You are not allowed to import any module
    
#4 Write a class Square that defines a square by: (based on 3-square.py)

    Private instance attribute: size:
    property def size(self): to retrieve it
    property setter def size(self, value): to set it:
    size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
    if size is less than 0, raise a ValueError exception with the message size must be >= 0
    Instantiation with optional size: def __init__(self, size=0):
    Public instance method: def area(self): that returns the current square area
    You are not allowed to import any module
    Why?

    Why a getter and setter?

    Reminder: size is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you       will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc.     Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.
    
#5 Write a class Square that defines a square by: (based on 4-square.py)

    Private instance attribute: size:
    property def size(self): to retrieve it
    property setter def size(self, value): to set it:
    size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
    if size is less than 0, raise a ValueError exception with the message size must be >= 0
    Instantiation with optional size: def __init__(self, size=0):
    Public instance method: def area(self): that returns the current square area
    Public instance method: def my_print(self): that prints in stdout the square with the character #:
    if size is equal to 0, print an empty line
    You are not allowed to import any module
    
#6 Write a class Square that defines a square by: (based on 5-square.py)

    Private instance attribute: size:
    property def size(self): to retrieve it
    property setter def size(self, value): to set it:
    size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
    if size is less than 0, raise a ValueError exception with the message size must be >= 0
    Private instance attribute: position:
    property def position(self): to retrieve it
    property setter def position(self, value): to set it:
    position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers
    Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
    Public instance method: def area(self): that returns the current square area
    Public instance method: def my_print(self): that prints in stdout the square with the character #:
    if size is equal to 0, print an empty line
    position should be use by using space - Don’t fill lines by spaces when position[1] > 0
    You are not allowed to import any module
