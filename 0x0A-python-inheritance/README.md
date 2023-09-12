# Python - Inheritance

> I love OOP!!. Object-oriented programming (OOP) offers a powerful concept known as `inheritance.` It allows us to model objects and programs as if they were part of real-world scenarios, with the added benefit of interaction with real people. A compelling analogy to illustrate this concept is the corporate world.

> In a workplace, you'll find various roles, such as Developers, Managers, Juniors, Seniors, Staff, and Contract Workers, among others. Inheritance helps us create a hierarchy among these roles. At its core, everyone in this context is an 'employee.' To avoid duplicating definitions for what makes someone an employee and what they can do, we start by defining the common attributes and capabilities shared by all employees.

> Then, we can move to more specific categories, like 'Developers.' Since developers are also employees, we can leverage inheritance by saying, `"Since a developer is an employee, they inherit all the qualities, rights, and privileges that an employee possesses"` This approach not only saves time but also ensures consistency.

> But inheritance doesn't stop there. We can further refine the hierarchy by specifying additional rights and privileges unique to developers. We can even delve deeper into the hierarchy by defining distinct rights for Junior and Senior Developers. This simple example of inheritance illustrates its power, but in practice, there's much more you can achieve with this fundamental OOP concept. It allows us to structure and organize our code in a way that closely mirrors the complexities of the real world, making OOP a valuable and versatile programming paradigm.


## Mandatory task

<details>
  <summary><code>0-lookup.py</code> - Python Function: Lookup Object Attributes and Methods</summary>
  <ul>
    <li>Prototype: <code>def lookup(obj)</code></li>
    <li>Returns a list object</li>
    <li>You are not allowed to import any module</li>
    <li>Example Usage and Expected Output provided</li>
  </ul>
</details>

<details>
  <summary>
    <code>1-my_list.py</code> - Write a class that inherits from a list
  </summary>
  <ul>
    <li>Public instance method: <code>def print_sorted(self)</code> that prints the list, but sorted (ascending sort)</li>
    <li>You can assume that all the elements of the list will be of type int</li>
    <li>You are not allowed to import any module</li>
    <li>Example Usage provided</li>
  </ul>
</details>

<details>
  <summary>
    <code>2-is_same_class.py</code> - Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.
  </summary>
  <ul>
    <li>Prototype: <code>def is_same_class(obj, a_class)</code></li>
    <li>You are not allowed to import any module</li>
    <li>Example Usage and Expected Output provided</li>
  </ul>
</details>

<details>
  <summary>
    <code>3-is_kind_of_class.py</code> - Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.
  </summary>
  <ul>
    <li>Prototype: <code>def is_kind_of_class(obj, a_class)</code></li>
    <li>You are not allowed to import any module</li>
    <li>Example Usage and Expected Output provided</li>
  </ul>
</details>

<details>
  <summary>
    <code>4-inherits_from.py</code> - Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
  </summary>
  <ul>
    <li>Prototype: <code>def inherits_from(obj, a_class)</code></li>
    <li>You are not allowed to import any module</li>
    <li>Example Usage and Expected Output provided</li>
  </ul>
</details>

<details>
  <summary>
    <code>5-base_geometry.py</code> - Write an empty class BaseGeometry.
  </summary>
  <ul>
    <li>You are not allowed to import any module</li>
    <li>Example Usage provided</li>
  </ul>
</details>


<details>
  <summary>
    <code>6-base_geometry.py</code> - Write a class BaseGeometry (based on 5-base_geometry.py).
  </summary>
  <ul>
    <li>Public instance method: <code>def area(self)</code> that raises an Exception with the message <code>area() is not implemented</code></li>
    <li>You are not allowed to import any module</li>
    <li>Example Usage provided</li>
  </ul>
</details>

<details>
  <summary>
    <code>7-base_geometry.py</code> - Write a class BaseGeometry (based on 6-base_geometry.py).
  </summary>
  <ul>
    <li>Public instance method: <code>def area(self)</code> that raises an Exception with the message <code>area() is not implemented</code></li>
    <li>Public instance method: <code>def integer_validator(self, name, value)</code> that validates value:
      <ul>
        <li>You can assume name is always a string</li>
        <li>If value is not an integer: raise a <code>TypeError</code> exception, with the message <code><name> must be an integer</code></li>
        <li>If value is less or equal to 0: raise a <code>ValueError</code> exception with the message <code><name> must be greater than 0</code></li>
      </ul>
    </li>
    <li>You are not allowed to import any module</li>
    <li>Example Usage provided</li>
  </ul>
</details>

<details>
  <summary>
    <code>8-rectangle.py</code> - Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
  </summary>
  <ul>
    <li>Instantiation with width and height: <code>def __init__(self, width, height)</code>:
      <ul>
        <li>Width and height must be private. No getter or setter</li>
        <li>Width and height must be positive integers, validated by <code>integer_validator</code></li>
      </ul>
    </li>
    <li>Example Usage provided</li>
  </ul>
</details>

<details>
  <summary>
    <code>9-rectangle.py</code> - Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
  </summary>
  <ul>
    <li>Instantiation with width and height: <code>def __init__(self, width, height)</code>:
      <ul>
        <li>Width and height must be private. No getter or setter</li>
        <li>Width and height must be positive integers, validated by <code>integer_validator</code></li>
      </ul>
    </li>
    <li>The <code>area()</code> method must be implemented</li>
    <li><code>print()</code> should print, and <code>str()</code> should return, the following rectangle description: <code>[Rectangle] &lt;width&gt;/&lt;height&gt;</code></li>
    <li>Example Usage provided</li>
  </ul>
</details>

<details>
  <summary>
    <code>10-square.py</code> - Write a class Square that inherits from Rectangle (9-rectangle.py).
  </summary>
  <ul>
    <li>Instantiation with size: <code>def __init__(self, size)</code>:
      <ul>
        <li>Size must be private. No getter or setter</li>
        <li>Size must be a positive integer, validated by <code>integer_validator</code></li>
      </ul>
    </li>
    <li>The <code>area()</code> method must be implemented</li>
    <li>Print() should print, and str() should return, the square description: <code>[Square] &lt;width&gt;/&lt;height&gt;</code></li>
    <li>Example Usage provided</li>
  </ul>
</details>

<details>
  <summary>
    <code>11-square.py</code> - Square #2
  </summary>
  <ul>
    <li>Instantiation with size: <code>def __init__(self, size)</code>:
      <ul>
        <li>Size must be private. No getter or setter</li>
        <li>Size must be a positive integer, validated by <code>integer_validator</code></li>
      </ul>
    </li>
    <li>The <code>area()</code> method must be implemented</li>
    <li>Print() should print, and str() should return, the square description: <code>[Square] &lt;width&gt;/&lt;height&gt;</code></li>
    <li>Example Usage provided</li>
  </ul>
</details>

## Advanced task
<details>
  <summary>
    <code>100-my_int.py</code> - My integer
  </summary>
  <ul>
    <li>Advanced task</li>
    <li>Write a class MyInt that inherits from int:
      <ul>
        <li>MyInt is a rebel. MyInt has == and != operators inverted</li>
        <li>You are not allowed to import any module</li>
      </ul>
    </li>
    <li>Example Usage provided</li>
  </ul>
</details>

<details>
  <summary>
    <code>101-add_attribute.py</code> - Can I?
  </summary>
  <ul>
    <li>Advanced task</li>
    <li>Write a function that adds a new attribute to an object if it’s possible:
      <ul>
        <li>Raise a TypeError exception, with the message <code>can't add new attribute</code> if the object can’t have a new attribute</li>
        <li>You are not allowed to use try/except</li>
        <li>You are not allowed to import any module</li>
      </ul>
    </li>
    <li>Example Usage provided</li>
  </ul>
</details>

