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
	- property `def position(self):` to retrieve it
	- property setter def position(self, value): to set it:
	- position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers
- Instantiation with optional size and optional position: `def __init__(self, size=0, position=(0, 0)):`

## Advanced

100. A class `Node` that defines a node of a singly linked list by:

- Private instance attribute: data:
	- property def `data(self):` to retrieve it
	- property setter `def data(self, value):` to set it:
	- data must be an integer, otherwise raise a TypeError exception with the message data must be an integer
- Private instance attribute: `next_node`:
	- property `def next_node(self):` to retrieve it
	- property setter `def next_node(self, value):` to set it:
	- next_node can be None or must be a Node, otherwise raise a TypeError exception with the message next_node must be a Node object
- Instantiation with data and next_node: `def __init__(self, data, next_node=None):`

- And, write a class `SinglyLinkedList` that defines a singly linked list by:

- Private instance attribute: head (no setter or getter)
- Simple instantiation: `def __init__(self):`
- Should be printable:
	- print the entire list in stdout
	- one node number by line
- Public instance method: `def sorted_insert(self, value):` that inserts a new Node into the correct sorted position in the list (increasing order)

101. Write a class Square that defines a square by: (based on `6-square.py`)
- Printing a Square instance should have the same behavior as my_print()
