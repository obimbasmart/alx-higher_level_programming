# Python - More Classes and Objects
> This project delves deep into the world of Python classes and objects, shedding light on essential concepts such as `class methods`, `static methods`,` class attributes`, and best practices. Prior to this project, I often found myself confused between static methods and class methods. However, through this project, I gained a clear understanding of the distinctions between these two and when to appropriately apply each

`0-rectangle.py` - Write an empty class Rectangle that defines a rectangle:

<details>
 <summary> <code>1-rectangle.py</code> - Write a class Rectangle that defines a rectangle.</summary>
 <ul>
  <li>Private instance attribute: width:
    <ul>
      <li>property def width(self): to retrieve it</li>
      <li>property setter def width(self, value): to set it:
        <ul>
          <li>width must be an integer, otherwise raise a TypeError exception with the message width must be an integer</li>
          <li>if width is less than 0, raise a ValueError exception with the message width must be >= 0</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Private instance attribute: height:
    <ul>
      <li>property def height(self): to retrieve it</li>
      <li>property setter def height(self, value): to set it:
        <ul>
          <li>height must be an integer, otherwise raise a TypeError exception with the message height must be an integer</li>
          <li>if height is less than 0, raise a ValueError exception with the message height must be >= 0</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Instantiation with optional width and height: <code>def __init__(self, width=0, height=0):</code></li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>


<details>
 <summary> <code>2-rectangle.py</code> - Write a class Rectangle that defines a rectangle.</summary>
 <ul>
  <li>Private instance attribute: width:
    <ul>
      <li>property def width(self): to retrieve it</li>
      <li>property setter def width(self, value): to set it:
        <ul>
          <li>width must be an integer, otherwise raise a TypeError exception with the message width must be an integer</li>
          <li>if width is less than 0, raise a ValueError exception with the message width must be >= 0</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Private instance attribute: height:
    <ul>
      <li>property def height(self): to retrieve it</li>
      <li>property setter def height(self, value): to set it:
        <ul>
          <li>height must be an integer, otherwise raise a TypeError exception with the message height must be an integer</li>
          <li>if height is less than 0, raise a ValueError exception with the message height must be >= 0</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Instantiation with optional width and height: <code>def __init__(self, width=0, height=0):</code></li>
  <li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
  <li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:
    <ul>
      <li>if width or height is equal to 0, perimeter is equal to 0</li>
    </ul>
  </li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

<details>
 <summary> <code>3-rectangle.py</code> - Write a class Rectangle that defines a rectangle.</summary>
 <ul>
  <li>Private instance attribute: width:
    <ul>
      <li>property def width(self): to retrieve it</li>
      <li>property setter def width(self, value): to set it:
        <ul>
          <li>width must be an integer, otherwise raise a TypeError exception with the message width must be an integer</li>
          <li>if width is less than 0, raise a ValueError exception with the message width must be >= 0</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Private instance attribute: height:
    <ul>
      <li>property def height(self): to retrieve it</li>
      <li>property setter def height(self, value): to set it:
        <ul>
          <li>height must be an integer, otherwise raise a TypeError exception with the message height must be an integer</li>
          <li>if height is less than 0, raise a ValueError exception with the message height must be >= 0</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Instantiation with optional width and height: <code>def __init__(self, width=0, height=0):</code></li>
  <li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
  <li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:
    <ul>
      <li>if width or height is equal to 0, perimeter has to be equal to 0</li>
    </ul>
  </li>
  <li><code>print()</code> and <code>str()</code> should print the rectangle with the character #: (see example below)
    <ul>
      <li>if width or height is equal to 0, return an empty string</li>
    </ul>
  </li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>


<details>
 <summary> <code>4-rectangle.py</code> - Write a class Rectangle that defines a rectangle.</summary>
 <ul>
  <li>Private instance attribute: width:
    <ul>
      <li>property def width(self): to retrieve it</li>
      <li>property setter def width(self, value): to set it:
        <ul>
          <li>width must be an integer, otherwise raise a TypeError exception with the message width must be an integer</li>
          <li>if width is less than 0, raise a ValueError exception with the message width must be >= 0</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Private instance attribute: height:
    <ul>
      <li>property def height(self): to retrieve it</li>
      <li>property setter def height(self, value): to set it:
        <ul>
          <li>height must be an integer, otherwise raise a TypeError exception with the message height must be an integer</li>
          <li>if height is less than 0, raise a ValueError exception with the message height must be >= 0</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Instantiation with optional width and height: <code>def __init__(self, width=0, height=0):</code></li>
  <li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
  <li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:
    <ul>
      <li>if width or height is equal to 0, perimeter has to be equal to 0</li>
    </ul>
  </li>
  <li><code>print()</code> and <code>str()</code> should print the rectangle with the character #: (see example below)
    <ul>
      <li>if width or height is equal to 0, return an empty string</li>
    </ul>
  </li>
  <li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> (see example below)</li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

<details>
 <summary> <code>5-rectangle.py</code> - Write a class Rectangle that defines a rectangle.</summary>
 <ul>
  <li>Private instance attribute: width:
    <ul>
      <li>property def width(self): to retrieve it</li>
      <li>property setter def width(self, value): to set it:
        <ul>
          <li>width must be an integer, otherwise raise a TypeError exception with the message width must be an integer</li>
          <li>if width is less than 0, raise a ValueError exception with the message width must be >= 0</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Private instance attribute: height:
    <ul>
      <li>property def height(self): to retrieve it</li>
      <li>property setter def height(self, value): to set it:
        <ul>
          <li>height must be an integer, otherwise raise a TypeError exception with the message height must be an integer</li>
          <li>if height is less than 0, raise a ValueError exception with the message height must be >= 0</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Instantiation with optional width and height: <code>def __init__(self, width=0, height=0):</code></li>
  <li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
  <li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:
    <ul>
      <li>if width or height is equal to 0, perimeter has to be equal to 0</li>
    </ul>
  </li>
  <li><code>print()</code> and <code>str()</code> should print the rectangle with the character #:
    <ul>
      <li>if width or height is equal to 0, return an empty string</li>
    </ul>
  </li>
  <li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code></li>
  <li>Print the message <code>Bye rectangle...</code> (3 dots, not ellipsis) when an instance of Rectangle is deleted</li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>


<details>
 <summary> <code>6-rectangle.py</code> - Write a class Rectangle that defines a rectangle.</summary>
 <ul>
  <li>Private instance attribute: width:
    <ul>
      <li>property def width(self): to retrieve it</li>
      <li>property setter def width(self, value): to set it:
        <ul>
          <li>width must be an integer, otherwise raise a TypeError exception with the message width must be an integer</li>
          <li>if width is less than 0, raise a ValueError exception with the message width must be >= 0</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Private instance attribute: height:
    <ul>
      <li>property def height(self): to retrieve it</li>
      <li>property setter def height(self, value): to set it:
        <ul>
          <li>height must be an integer, otherwise raise a TypeError exception with the message height must be an integer</li>
          <li>if height is less than 0, raise a ValueError exception with the message height must be >= 0</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Public class attribute: <code>number_of_instances</code>:
    <ul>
      <li>Initialized to 0</li>
      <li>Incremented during each new instance instantiation</li>
      <li>Decremented during each instance deletion</li>
    </ul>
  </li>
  <li>Instantiation with optional width and height: <code>def __init__(self, width=0, height=0):</code></li>
  <li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
  <li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:
    <ul>
      <li>if width or height is equal to 0, perimeter has to be equal to 0</li>
    </ul>
  </li>
  <li><code>print()</code> and <code>str()</code> should print the rectangle with the character #:
    <ul>
      <li>if width or height is equal to 0, return an empty string</li>
    </ul>
  </li>
  <li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by
 </details>
<details>
 <summary> <code>6-rectangle.py</code> - Write a class Rectangle that defines a rectangle.</summary>
 <ul>
  <li>Private instance attribute: <code>width</code>:
    <ul>
      <li>property def width(self): to retrieve it</li>
      <li>property setter def width(self, value): to set it:
        <ul>
          <li>width must be an integer, otherwise raise a TypeError exception with the message width must be an integer</li>
          <li>if width is less than 0, raise a ValueError exception with the message width must be >= 0</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Private instance attribute: <code>height</code>:
    <ul>
      <li>property def height(self): to retrieve it</li>
      <li>property setter def height(self, value): to set it:
        <ul>
          <li>height must be an integer, otherwise raise a TypeError exception with the message height must be an integer</li>
          <li>if height is less than 0, raise a ValueError exception with the message height must be >= 0</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Public class attribute: <code>number_of_instances</code>:
    <ul>
      <li>Initialized to 0</li>
      <li>Incremented during each new instance instantiation</li>
      <li>Decremented during each instance deletion</li>
    </ul>
  </li>
  <li>Public class attribute: <code>print_symbol</code>:
    <ul>
      <li>Initialized to #</li>
      <li>Used as symbol for string representation</li>
      <li>Can be any type</li>
    </ul>
  </li>
  <li>Instantiation with optional width and height: <code>def __init__(self, width=0, height=0):</code></li>
  <li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
  <li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:
    <ul>
      <li>if width or height is equal to 0, perimeter has to be equal to 0</li>
    </ul>
  </li>
  <li><code>print()</code> and <code>str()</code> should print the rectangle with the character(s) stored in <code>print_symbol</code>:
    <ul>
      <li>if width or height is equal to 0, return an empty string</li>
    </ul>
  </li>
  <li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code></li>
  <li>Print the message <code>Bye rectangle...</code> (3 dots, not ellipsis) when an instance of Rectangle is deleted</li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

<details>
 <summary> <code>8-rectangle.py</code> - Write a class Rectangle that defines a rectangle.</summary>
 <ul>
  <li>Private instance attribute: <code>width</code>:
    <ul>
      <li>property def width(self): to retrieve it</li>
      <li>property setter def width(self, value): to set it:
        <ul>
          <li>width must be an integer, otherwise raise a TypeError exception with the message width must be an integer</li>
          <li>if width is less than 0, raise a ValueError exception with the message width must be >= 0</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Private instance attribute: <code>height</code>:
    <ul>
      <li>property def height(self): to retrieve it</li>
      <li>property setter def height(self, value): to set it:
        <ul>
          <li>height must be an integer, otherwise raise a TypeError exception with the message height must be an integer</li>
          <li>if height is less than 0, raise a ValueError exception with the message height must be >= 0</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Public class attribute: <code>number_of_instances</code>:
    <ul>
      <li>Initialized to 0</li>
      <li>Incremented during each new instance instantiation</li>
      <li>Decremented during each instance deletion</li>
    </ul>
  </li>
  <li>Public class attribute: <code>print_symbol</code>:
    <ul>
      <li>Initialized to #</li>
      <li>Used as symbol for string representation</li>
      <li>Can be any type</li>
    </ul>
  </li>
  <li>Instantiation with optional width and height: <code>def __init__(self, width=0, height=0):</code></li>
  <li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
  <li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:
    <ul>
      <li>if width or height is equal to 0, perimeter has to be equal to 0</li>
    </ul>
  </li>
  <li><code>print()</code> and <code>str()</code> should print the rectangle with the character #:
    <ul>
      <li>if width or height is equal to 0, return an empty string</li>
    </ul>
  </li>
  <li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code></li>
  <li>Print the message <code>Bye rectangle...</code> (3 dots, not ellipsis) when an instance of Rectangle is deleted</li>
  <li>Static method <code>def bigger_or_equal(rect_1, rect_2):</code> that returns the biggest rectangle based on the area
    <ul>
      <li>rect_1 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_1 must be an instance of Rectangle</li>
      <li>rect_2 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_2 must be an instance of Rectangle</li>
      <li>Returns rect_1 if both have the same area value</li>
    </ul>
  </li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

<details>
 <summary> <code>9-rectangle.py</code> - Write a class Rectangle that defines a rectangle.</summary>
 <ul>
  <li>Private instance attribute: <code>width</code>:
    <ul>
      <li>property def width(self): to retrieve it</li>
      <li>property setter def width(self, value): to set it:
        <ul>
          <li>width must be an integer, otherwise raise a TypeError exception with the message width must be an integer</li>
          <li>if width is less than 0, raise a ValueError exception with the message width must be >= 0</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Private instance attribute: <code>height</code>:
    <ul>
      <li>property def height(self): to retrieve it</li>
      <li>property setter def height(self, value): to set it:
        <ul>
          <li>height must be an integer, otherwise raise a TypeError exception with the message height must be an integer</li>
          <li>if height is less than 0, raise a ValueError exception with the message height must be >= 0</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Public class attribute: <code>number_of_instances</code>:
    <ul>
      <li>Initialized to 0</li>
      <li>Incremented during each new instance instantiation</li>
      <li>Decremented during each instance deletion</li>
    </ul>
  </li>
  <li>Public class attribute: <code>print_symbol</code>:
    <ul>
      <li>Initialized to #</li>
      <li>Used as a symbol for string representation</li>
      <li>Can be any type</li>
    </ul>
  </li>
  <li>Instantiation with optional width and height: <code>def __init__(self, width=0, height=0):</code></li>
  <li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
  <li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:
    <ul>
      <li>if width or height is equal to 0, perimeter has to be equal to 0</li>
    </ul>
  </li>
  <li><code>print()</code> and <code>str()</code> should print the rectangle with the character #:
    <ul>
      <li>if width or height is equal to 0, return an empty string</li>
    </ul>
  </li>
  <li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code></li>
  <li>Print the message <code>Bye rectangle...</code> (3 dots, not ellipsis) when an instance of Rectangle is deleted</li>
  <li>Static method <code>def bigger_or_equal(rect_1, rect_2):</code> that returns the biggest rectangle based on the area
    <ul>
      <li>rect_1 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_1 must be an instance of Rectangle</li>
      <li>rect_2 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_2 must be an instance of Rectangle</li>
      <li>Returns rect_1 if both have the same area value</li>
    </ul>
  </li>
  <li>Class method <code>def square(cls, size=0):</code> that returns a new Rectangle instance with width == height == size</li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>





