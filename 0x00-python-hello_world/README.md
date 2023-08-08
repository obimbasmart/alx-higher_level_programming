# Python - Hellow World

## Mandatory
0. Write a Shell script that runs a Python script.
    - The Python file name will be saved in the environment variable `$PYFILE`
1. Write a Shell script that runs Python code.

    - The Python code will be saved in the environment variable `$PYCODE`
2. Write a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.
    - Use the function `print`

3. <details><summary>Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.</summary>
    <ul>
        <li>You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py)</li>
        <li>The output of the script should be:
the number, followed by `Battery street`,
followed by a new line</li>
        <li>You are not allowed to cast the variable number into a string</li>
        <li>Your code must be 3 lines long</li>
        <li>You have to use f-strings</li>
    </ul>
  </details>

4. Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.
    - You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/4-print_float.py)
5. Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.
6. Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py) in order to print 3 times a string stored in the variable str, followed by its first 9 characters.
7. Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/6-concat.py) to print Welcome to Holberton School!
8. Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py) to print object-oriented programming with Python, followed by a new line.
9. Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.
    - Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py)
10. Write a function in C that checks if a singly linked list has a cycle in it.
    - Prototype: `int check_cycle(listint_t *list);`
    - Return: 0 if there is no cycle, 1 if there is a cycle

## Advanced
1. Write a Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.
    - Use the function write from the sys module
    - You are not allowed to use print
    - Your script should print to stderr
    - Your script should exit with the status code 1
2. Write a script that compiles a Python script file.
    - The Python file name will be stored in the environment variable $PYFILE
    - The output filename has to be $PYFILEc (ex: export PYFILE=my_main.py => output filename: my_main.pyc)
3. Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:
    ```C
         3           0 LOAD_CONST               1 (98)
                      3 LOAD_FAST                0 (a)
                      6 LOAD_FAST                1 (b)
                      9 BINARY_POWER
                     10 BINARY_ADD
                     11 RETURN_VALUE
    ```
    
