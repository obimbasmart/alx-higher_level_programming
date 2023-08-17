# Python - More Data Structures: Set, Dictionary

> 🐍 Python Adventures: Still on data structures: Sets, and Dictionaries 📚

> Upon finishing this project, I had to admit that python is just cool and makes coding fun. I really loved the `map, filter, reduce` family functions - they're powerful. While some wizards like `Guido van Rossum`  might not be the biggest fans of them I couldn't help but fall in love with their magic.

>  In one of the advanced task, I delved into the depths of nested maps! 🗺️ I crafted an incantation that looked something like this:

> <code>(list(map(lambda row: list(map(lambda n: n ** 2, row)), matrix)))</code>

Python is just cool !!!!!!!!!

> Yet in the end, it was a bittersweet project - I had to deal with `CPython` again - so much learning


## Madatory task


<details>
 <summary> <code>0-square_matrix_simple.py</code> - Write a function that computes the square value of all integers of a matrix.</summary>
 <ul>
  <li>Prototype: <code>def square_matrix_simple(matrix=[]):</code></li>
  <li><code>matrix</code> is a 2 dimensional array</li>
  <li>Returns a new matrix:
    <ul>
      <li>Same size as <code>matrix</code></li>
      <li>Each value should be the square of the value of the input</li>
    </ul>
  </li>
  <li>Initial matrix should not be modified</li>
  <li>You are not allowed to import any module</li>
  <li>You are allowed to use regular loops, map, etc.</li>
 </ul>
</details>

Feel free to use this formatted text for your purpose.

<details>
 <summary> <code>1-search_replace.py</code> - Write a function that replaces all occurrences of an element by another in a new list.</summary>
 <ul>
  <li>Prototype: <code>def search_replace(my_list, search, replace):</code></li>
  <li><code>my_list</code> is the initial list</li>
  <li><code>search</code> is the element to replace in the list</li>
  <li><code>replace</code> is the new element</li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

<details>
 <summary> <code>2-uniq_add.py</code> - Write a function that adds all unique integers in a list (only once for each integer).</summary>
 <ul>
  <li>Prototype: <code>def uniq_add(my_list=[]):</code></li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

<details>
 <summary> <code>3-common_elements.py</code> - Write a function that returns a set of common elements in two sets.</summary>
 <ul>
  <li>Prototype: <code>def common_elements(set_1, set_2):</code></li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

<details>
 <summary> <code>4-only_diff_elements.py</code> - Write a function that returns a set of all elements present in only one set.</summary>
 <ul>
  <li>Prototype: <code>def only_diff_elements(set_1, set_2):</code></li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

<details>
 <summary> <code>5-number_keys.py</code> - Write a function that returns the number of keys in a dictionary.</summary>
 <ul>
  <li>Prototype: <code>def number_keys(a_dictionary):</code></li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>
<details>
 <summary> <code>6-print_sorted_dictionary.py</code> - Write a function that prints a dictionary by ordered keys.</summary>
 <ul>
  <li>Prototype: <code>def print_sorted_dictionary(a_dictionary):</code></li>
  <li>You can assume that all keys are strings</li>
  <li>Keys should be sorted by alphabetic order</li>
  <li>Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)</li>
  <li>Dictionary values can have any type</li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

Certainly! Here's the information you provided with the proper formatting:


<details>
 <summary> <code>7-update_dictionary.py</code> - Write a function that replaces or adds key/value in a dictionary.</summary>
 <ul>
  <li>Prototype: <code>def update_dictionary(a_dictionary, key, value):</code></li>
  <li><code>key</code> argument will be always a string</li>
  <li><code>value</code> argument will be any type</li>
  <li>If a key exists in the dictionary, the value will be replaced</li>
  <li>If a key doesn’t exist in the dictionary, it will be created</li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

<details>
 <summary> <code>8-simple_delete.py</code> - Write a function that deletes a key in a dictionary.</summary>
 <ul>
  <li>Prototype: <code>def simple_delete(a_dictionary, key=""):</code></li>
  <li><code>key</code> argument will be always a string</li>
  <li>If a key doesn’t exist, the dictionary won’t change</li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>


<details>
 <summary> <code>9-multiply_by_2.py</code> - Write a function that returns a new dictionary with all values multiplied by 2.</summary>
 <ul>
  <li>Prototype: <code>def multiply_by_2(a_dictionary):</code></li>
  <li>You can assume that all values are only integers</li>
  <li>Returns a new dictionary</li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

<details>
 <summary> <code>10-best_score.py</code> - Write a function that returns a key with the biggest integer value.</summary>
 <ul>
  <li>Prototype: <code>def best_score(a_dictionary):</code></li>
  <li>You can assume that all values are only integers</li>
  <li>If no score found, return <code>None</code></li>
  <li>You can assume all students have a different score</li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

<details>
 <summary> <code>11-multiply_list_map.py</code> - Write a function that returns a list with all values multiplied by a number without using any loops.</summary>
 <ul>
  <li>Prototype: <code>def multiply_list_map(my_list=[], number=0):</code></li>
  <li>Returns a new list:
    <ul>
      <li>Same length as <code>my_list</code></li>
      <li>Each value should be multiplied by <code>number</code></li>
    </ul>
  </li>
  <li>Initial list should not be modified</li>
  <li>You are not allowed to import any module</li>
  <li>You have to use <code>map</code></li>
  <li>Your file should be max 3 lines</li>
 </ul>
</details>

<details>
 <summary> <code>12-roman_to_int.py</code> - Create a function <code>def roman_to_int(roman_string):</code> that converts a Roman numeral to an integer.</summary>
 <ul>
  <li>You can assume the number will be between 1 to 3999.</li>
  <li><code>def roman_to_int(roman_string)</code> must return an integer</li>
  <li>If the <code>roman_string</code> is not a string or <code>None</code>, return 0</li>
 </ul>
</details>

## Advancedt task

<details>
 <summary> <code>100-weight_average.py</code> - Write a function that returns the weighted average of all integers tuple (<code>&lt;score&gt;</code>, <code>&lt;weight&gt;</code>)</summary>
 <ul>
  <li>Prototype: <code>def weight_average(my_list=[]):</code></li>
  <li>Returns 0 if the list is empty</li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

<details>
 <summary> <code>101-square_matrix_map.py</code> - Write a function that computes the square value of all integers of a matrix using <code>map</code></summary>
 <ul>
  <li>Prototype: <code>def square_matrix_map(matrix=[]):</code></li>
  <li><code>matrix</code> is a 2 dimensional array</li>
  <li>Returns a new matrix:
    <ul>
      <li>Same size as <code>matrix</code></li>
      <li>Each value should be the square of the value of the input</li>
    </ul>
  </li>
  <li>Initial matrix should not be modified</li>
  <li>You are not allowed to import any module</li>
  <li>You have to use <code>map</code></li>
  <li>You are not allowed to use <code>for</code> or <code>while</code></li>
  <li>Your file should be max 3 lines</li>
 </ul>
</details>

<details>
 <summary> <code>102-complex_delete.py</code> - Write a function that deletes keys with a specific value in a dictionary.</summary>
 <ul>
  <li>Prototype: <code>def complex_delete(a_dictionary, value):</code></li>
  <li>If the value doesn’t exist, the dictionary won’t change</li>
  <li>All keys having the searched value have to be deleted</li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

<details>
 <summary> <code>103-python.c</code> - Create two C functions that print some basic info about Python lists and Python bytes objects.</summary>
 <ul>
  <li>Python lists:
    <ul>
      <li>Prototype: <code>void print_python_list(PyObject *p);</code></li>
      <li>Format: see example</li>
    </ul>
  </li>
  <li>Python bytes:
    <ul>
      <li>Prototype: <code>void print_python_bytes(PyObject *p);</code></li>
      <li>Format: see example</li>
      <li>Line “first X bytes”: print a maximum of 10 bytes</li>
      <li>If <code>p</code> is not a valid <code>PyBytesObject</code>, print an error message (see example)</li>
    </ul>
  </li>
  <li>About:
    <ul>
      <li>Python version: 3.4</li>
      <li>Your shared library will be compiled with this command line: <code>gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c</code></li>
      <li>You are not allowed to use the following macros/functions:
        <ul>
          <li><code>Py_SIZE</code></li>
          <li><code>Py_TYPE</code></li>
          <li><code>PyList_GetItem</code></li>
          <li><code>PyBytes_AS_STRING</code></li>
          <li><code>PyBytes_GET_SIZE</code></li>
        </ul>
      </li>
    </ul>
  </li>
 </ul>
</details>

