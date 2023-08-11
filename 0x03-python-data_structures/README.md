# Python - Data Structures: Lists, Tuples

## Mandatory tasks

<details>
 <summary> <code>0-print_list_integer.py</code> - Write a function that prints all integers of a list.</summary>
 <ul>
  <li>Prototype: <code>def print_list_integer(my_list=[]):</code></li>
  <li>Format: one integer per line. See example</li>
  <li>You are not allowed to import any module</li>
  <li>You can assume that the list only contains integers</li>
  <li>You are not allowed to cast integers into strings</li>
  <li>You have to use <code>str.format()</code> to print integers</li>
 </ul>
</details>

<details>
 <summary> <code>1-element_at.py</code> - Write a function that retrieves an element from a list like in C.</summary>
 <ul>
  <li>Prototype: <code>def element_at(my_list, idx):</code></li>
  <li>If <code>idx</code> is negative, the function should return <code>None</code></li>
  <li>If <code>idx</code> is out of range (> number of elements in <code>my_list</code>), the function should return <code>None</code></li>
  <li>You are not allowed to import any module</li>
  <li>You are not allowed to use <code>try/except</code></li>
 </ul>
</details>

<details>
 <summary> <code>2-replace_in_list.py</code> - Write a function that replaces an element of a list at a specific position (like in C).</summary>
 <ul>
  <li>Prototype: <code>def replace_in_list(my_list, idx, element):</code></li>
  <li>If <code>idx</code> is negative, the function should not modify anything, and returns the original list</li>
  <li>If <code>idx</code> is out of range (> number of elements in <code>my_list</code>), the function should not modify anything, and returns the original list</li>
  <li>You are not allowed to import any module</li>
  <li>You are not allowed to use <code>try/except</code></li>
 </ul>
</details>


<details>
 <summary> <code>3-print_reversed_list_integer.py</code> - Write a function that prints all integers of a list, in reverse order.</summary>
 <ul>
  <li>Prototype: <code>def print_reversed_list_integer(my_list=[]):</code></li>
  <li>Format: one integer per line. See example</li>
  <li>You are not allowed to import any module</li>
  <li>You can assume that the list only contains integers</li>
  <li>You are not allowed to cast integers into strings</li>
  <li>You have to use <code>str.format()</code> to print integers</li>
 </ul>
</details>

<details>
 <summary> <code>4-new_in_list.py</code> - Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).</summary>
 <ul>
  <li>Prototype: <code>def new_in_list(my_list, idx, element):</code></li>
  <li>If <code>idx</code> is negative, the function should return a copy of the original list</li>
  <li>If <code>idx</code> is out of range (> number of elements in <code>my_list</code>), the function should return a copy of the original list</li>
  <li>You are not allowed to import any module</li>
  <li>You are not allowed to use <code>try/except</code></li>
 </ul>
</details>


<details>
 <summary> <code>5-no_c.py</code> - Write a function that removes all characters c and C from a string.</summary>
 <ul>
  <li>Prototype: <code>def no_c(my_string):</code></li>
  <li>The function should return the new string</li>
  <li>You are not allowed to import any module</li>
  <li>You are not allowed to use <code>str.replace()</code></li>
 </ul>
</details>

<details>
 <summary> <code>6-print_matrix_integer.py</code> - Write a function that prints a matrix of integers.</summary>
 <ul>
  <li>Prototype: <code>def print_matrix_integer(matrix=[[]]):</code></li>
  <li>Format: see example</li>
  <li>You are not allowed to import any module</li>
  <li>You can assume that the list only contains integers</li>
  <li>You are not allowed to cast integers into strings</li>
  <li>You have to use <code>str.format()</code> to print integers</li>
 </ul>
</details>

<details>
 <summary> <code>7-add_tuple.py</code> - Write a function that adds 2 tuples.</summary>
 <ul>
  <li>Prototype: <code>def add_tuple(tuple_a=(), tuple_b=()):</code></li>
  <li>Returns a tuple with 2 integers:</li>
  <ul>
   <li>The first element should be the addition of the first element of each argument</li>
   <li>The second element should be the addition of the second element of each argument</li>
  </ul>
  <li>You are not allowed to import any module</li>
  <li>You can assume that the two tuples will only contain integers</li>
  <li>If a tuple is smaller than 2, use the value 0 for each missing integer</li>
  <li>If a tuple is bigger than 2, use only the first 2 integers</li>
 </ul>
</details>

<details>
 <summary> <code>8-multiple_returns(sentence)</code> - Write a function that returns a tuple with the length of a string and its first character.</summary>
 <ul>
  <li>If the sentence is empty, the first character should be equal to None</li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>


<details>
 <summary> <code>9-max_integer.py</code> - Write a function that finds the biggest integer of a list.</summary>
 <ul>
  <li>If the list is empty, return None</li>
  <li>You can assume that the list only contains integers</li>
  <li>You are not allowed to import any module</li>
  <li>You are not allowed to use the builtin <code>max()</code></li>
 </ul>
</details>


<details>
 <summary> <code>10-divisible_by_2(my_list=[])</code> - Write a function that finds all multiples of 2 in a list.</summary>
 <ul>
  <li>Return a new list with True or False, depending on whether the integer at the same position in the original list is a multiple of 2</li>
  <li>The new list should have the same size as the original list</li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

<details>
 <summary> <code>11-delete_at(my_list=[], idx=0)</code> - Write a function that deletes the item at a specific position in a list.</summary>
 <ul>
  <li>If idx is negative or out of range, nothing changes (returns the same list)</li>
  <li>You are not allowed to use pop()</li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

<details>
 <summary> <code>12-switch.py</code> - Complete the source code to switch the value of a and b</summary>
 <ul>
  <li>You can find the source code <a href="https://github.com/alx-tools/0x03.py/blob/master/12-switch.py">here</a></li>
  <li>Your code should be inserted where the comment is (line 4)</li>
  <li>Your program should be exactly 5 lines long</li>
 </ul>
</details>

<details>
 <summary> <code>13-is_palindrome.c</code> - Write a function in C that checks if a singly linked list is a palindrome</summary>
 <ul>
  <li>Prototype: <code>int is_palindrome(listint_t **head);</code></li>
  <li>Return: <code>0</code> if it is not a palindrome, <code>1</code> if it is a palindrome</li>
  <li>An empty list is considered a palindrome</li>
 </ul>
</details>


