# Python - More Classes and Objects

## Mandatory

0. An empty class `Rectangle` that defines a rectangle:
1. Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)

- Private instance attribute: width:
- property def width(self): to retrieve it
- property setter def width(self, value): to set it:
    - width must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
    - if width is less than 0, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: height:
    - property `def height(self):` to retrieve it
    - property setter `def height(self, value):` to set it:
    - height must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
    - if height is less than 0, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional width and height: `def __init__(self, width=0, height=0):`

2. A class Rectangle that defines a rectangle by: (based on 1-rectangle.py)
- Public instance method: def area(self): that returns the rectangle area
- Public instance method: def perimeter(self): that returns the rectangle perimeter:
    - if width or height is equal to 0, perimeter is equal to 0

3. A class Rectangle that defines a rectangle by: (based on `2-rectangle.py`)
- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
- if width or height is equal to 0, return an empty string

4. A class Rectangle that defines a rectangle by: (based on `3-rectangle.py`)
- `repr()` should return a string representation of the rectangle to be 
able to recreate a new instance by using `eval()`

5. A class Rectangle that defines a rectangle by: (based on `4-rectangle.py`)
- Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) 
when an instance of Rectangle is deleted

6. A class Rectangle that defines a rectangle by: (based on `5-rectangle.py`)
- Public class attribute `number_of_instances`:
    - Initialized to 0 
    - Incremented during each new instance instantiation 
    - Decremented during each instance deletion