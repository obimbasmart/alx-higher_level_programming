# Python - Classes and Objects

## Mandatory

0. An empty class Square that defines a square
1. A class Square that defines a square by: (based on `0-square.py`)
	- Private instance attribute: size
	- Instantiation with size (no type/value verification)
	- You are not allowed to import any module

2. A class Square that defines a square by: (based on `1-square.py`)
	- size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
	- if size is less than 0, raise a ValueError exception with the message size must be >= 0

3. A class Square that defines a square by: (based on `2-square.py`)
	- Public instance method: `def area(self)`: that returns the current square area

4. A class Square that defines a square by: (based on `3-square.py`)
	- Private instance attribute: size:
		- property `def size(self):` to retrieve it
		- property setter `def size(self, value):` to set it

5.  a class Square that defines a square by: (based on `4-square.py`)
	- Public instance method: `def my_print(self):` that prints in stdout the square with the character #:
		- if size is equal to 0, print an empty line

6. Private instance attribute: position:
	- property def position(self): to retrieve it
	- property setter def position(self, value): to set it:
	- position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers
- Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
