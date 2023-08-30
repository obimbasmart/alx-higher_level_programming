## Mandatory

# Python - Classes and Objects
> The whole concept of OOP is cool, yeah – the idea of bundling data and methods in an object brings a new level of elegance to coding. I hereby welcome myself to Object-Oriented Programming 

## Mandatory

`0-square.py` - Write an empty class Square that defines a square:
- You are not allowed to import any modules.

<details>
 <summary> <code>1-square.py</code> - Write a class <code>Square</code> that defines a square by:</summary>
 <ul>
  <li>Private instance attribute: <code>size</code></li>
  <li>Instantiation with <code>size</code> (no type/value verification)</li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

<details>
 <summary> <code>2-square.py</code> - Write a class <code>Square</code> that defines a square by:</summary>
 <ul>
  <li>Private instance attribute: <code>size</code></li>
  <li>Instantiation with optional size: <code>def __init__(self, size=0):</code></li>
  <li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code></li>
  <li>If <code>size</code> is less than 0, raise a <code>ValueError</code> exception with the message <code>size must be >= 0</code></li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

<details>
 <summary> <code>3-square.py</code> - Write a class <code>Square</code> that defines a square by:</summary>
 <ul>
  <li>Private instance attribute: <code>size</code></li>
  <li>Instantiation with optional size: <code>def __init__(self, size=0):</code></li>
  <li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code></li>
  <li>If <code>size</code> is less than 0, raise a <code>ValueError</code> exception with the message <code>size must be >= 0</code></li>
  <li>Public instance method: <code>def area(self):</code> that returns the current square area</li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

<details>
 <summary> <code>4-square.py</code> - Write a class <code>Square</code> that defines a square by:</summary>
 <ul>
  <li>Private instance attribute: <code>size:</code></li>
  <li>Property <code>def size(self):</code> to retrieve it</li>
  <li>Property setter <code>def size(self, value):</code> to set it:</li>
  <ul>
    <li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code></li>
    <li>If <code>size</code> is less than 0, raise a <code>ValueError</code> exception with the message <code>size must be >= 0</code></li>
  </ul>
  <li>Instantiation with optional size: <code>def __init__(self, size=0):</code></li>
  <li>Public instance method: <code>def area(self):</code> that returns the current square area</li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

<details>
 <summary> <code>5-square.py</code> - Write a class <code>Square</code> that defines a square by:</summary>
 <ul>
  <li>Private instance attribute: <code>size:</code></li>
  <li>Property <code>def size(self):</code> to retrieve it</li>
  <li>Property setter <code>def size(self, value):</code> to set it:</li>
  <ul>
    <li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code></li>
    <li>If <code>size</code> is less than 0, raise a <code>ValueError</code> exception with the message <code>size must be >= 0</code></li>
  </ul>
  <li>Instantiation with optional size: <code>def __init__(self, size=0):</code></li>
  <li>Public instance method: <code>def area(self):</code> that returns the current square area</li>
  <li>Public instance method: <code>def my_print(self):</code> that prints in <code>stdout</code> the square with the character #:</li>
  <ul>
    <li>If size is equal to 0, print an empty line</li>
  </ul>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

<details>
 <summary> <code>6-square.py</code> - Write a class <code>Square</code> that defines a square by:</summary>
 <ul>
  <li>Private instance attribute: <code>size:</code></li>
  <li>Property <code>def size(self):</code> to retrieve it</li>
  <li>Property setter <code>def size(self, value):</code> to set it:</li>
  <ul>
    <li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code></li>
    <li>If <code>size</code> is less than 0, raise a <code>ValueError</code> exception with the message <code>size must be >= 0</code></li>
  </ul>
  <li>Private instance attribute: <code>position:</code></li>
  <li>Property <code>def position(self):</code> to retrieve it</li>
  <li>Property setter <code>def position(self, value):</code> to set it:</li>
  <ul>
    <li><code>position</code> must be a tuple of 2 positive integers, otherwise raise a <code>TypeError</code> exception with the message <code>position must be a tuple of 2 positive integers</code></li>
  </ul>
  <li>Instantiation with optional size and optional position: <code>def __init__(self, size=0, position=(0, 0)):</code></li>
  <li>Public instance method: <code>def area(self):</code> that returns the current square area</li>
  <li>Public instance method: <code>def my_print(self):</code> that prints in <code>stdout</code> the square with the character #:</li>
  <ul>
    <li>If size is equal to 0, print an empty line</li>
    <li>Position should be used by using space - Don’t fill lines by spaces when position[1] > 0</li>
  </ul>
  <li>You are not allowed to import any module</li>
 </ul>
</details>


<details>
 <summary> <code>100-singly_linked_list.py</code> - Write a class <code>Node</code> that defines a node of a singly linked list by:</summary>
 <ul>
  <li>Private instance attribute: <code>data:</code></li>
  <li>Property <code>def data(self):</code> to retrieve it</li>
  <li>Property setter <code>def data(self, value):</code> to set it:</li>
  <ul>
    <li><code>data</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>data must be an integer</code></li>
  </ul>
  <li>Private instance attribute: <code>next_node:</code></li>
  <li>Property <code>def next_node(self):</code> to retrieve it</li>
  <li>Property setter <code>def next_node(self, value):</code> to set it:</li>
  <ul>
    <li><code>next_node</code> can be <code>None</code> or must be a <code>Node</code>, otherwise raise a <code>TypeError</code> exception with the message <code>next_node must be a Node object</code></li>
  </ul>
  <li>Instantiation with data and next_node: <code>def __init__(self, data, next_node=None):</code></li>
 </ul>
</details>

<details>
 <summary> <code>100-singly_linked_list.py</code> - Write a class <code>SinglyLinkedList</code> that defines a singly linked list by:</summary>
 <ul>
  <li>Private instance attribute: <code>head</code> (no setter or getter)</li>
  <li>Simple instantiation: <code>def __init__(self):</code></li>
  <li>Should be printable: print the entire list in <code>stdout</code>, one node number per line</li>
  <li>Public instance method: <code>def sorted_insert(self, value):</code> that inserts a new <code>Node</code> into the correct sorted position in the list (increasing order)</li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>


<details>
 <summary> <code>101-square.py</code> - Write a class <code>Square</code> that defines a square by:</summary>
 <ul>
  <li>Private instance attribute: <code>size:</code></li>
  <li>Property <code>def size(self):</code> to retrieve it</li>
  <li>Property setter <code>def size(self, value):</code> to set it:</li>
  <ul>
    <li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code></li>
    <li>If <code>size</code> is less than 0, raise a <code>ValueError</code> exception with the message <code>size must be >= 0</code></li>
  </ul>
  <li>Private instance attribute: <code>position:</code></li>
  <li>Property <code>def position(self):</code> to retrieve it</li>
  <li>Property setter <code>def position(self, value):</code> to set it:</li>
  <ul>
    <li><code>position</code> must be a tuple of 2 positive integers, otherwise raise a <code>TypeError</code> exception with the message <code>position must be a tuple of 2 positive integers</code></li>
  </ul>
  <li>Instantiation with optional size and optional position: <code>def __init__(self, size=0, position=(0, 0)):</code></li>
  <li>Public instance method: <code>def area(self):</code> that returns the current square area</li>
  <li>Public instance method: <code>def my_print(self):</code> that prints in <code>stdout</code> the square with the character #:</li>
  <ul>
    <li>If size is equal to 0, print an empty line</li>
    <li>Position should be used by using space</li>
    <li>Printing a <code>Square</code> instance should have the same behavior as <code>my_print()</code></li>
  </ul>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

<details>
 <summary> <code>102-square.py</code> - Write a class <code>Square</code> that defines a square by:</summary>
 <ul>
  <li>Private instance attribute: <code>size:</code></li>
  <li>Property <code>def size(self):</code> to retrieve it</li>
  <li>Property setter <code>def size(self, value):</code> to set it:</li>
  <ul>
    <li><code>size</code> must be a number (float or integer), otherwise raise a <code>TypeError</code> exception with the message <code>size must be a number</code></li>
    <li>If <code>size</code> is less than 0, raise a <code>ValueError</code> exception with the message <code>size must be >= 0</code></li>
  </ul>
  <li>Instantiation with size: <code>def __init__(self, size=0):</code></li>
  <li>Public instance method: <code>def area(self):</code> that returns the current square area</li>
  <li><code>Square</code> instance can answer to comparators: <code>==</code>, <code>!=</code>, <code>></code>, <code>>=</code>, <code><</code> and <code><=</code> based on the square area</li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>




