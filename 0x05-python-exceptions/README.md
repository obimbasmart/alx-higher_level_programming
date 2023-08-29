# Python Exception
> For me, Python exception handling is like having a safety net while traversing the coding landscape. It's the art of anticipating errors and crafting elegant solutions that allow programs to gracefully recover

## Mandatory
<details>
 <summary> <code>0-safe_print_list.py</code> - Write a function that prints x elements of a list.</summary>
 <ul>
  <li>Prototype: <code>def safe_print_list(my_list=[], x=0):</code></li>
  <li><code>my_list</code> can contain any type (integer, string, etc.)</li>
  <li>All elements must be printed on the same line followed by a new line.</li>
  <li><code>x</code> represents the number of elements to print</li>
  <li><code>x</code> can be bigger than the length of <code>my_list</code></li>
  <li>Returns the real number of elements printed</li>
  <li>You have to use <code>try:</code> / <code>except:</code></li>
  <li>You are not allowed to import any module</li>
  <li>You are not allowed to use <code>len()</code></li>
 </ul>
</details>

<details>
 <summary> <code>1-safe_print_integer.py</code> - Write a function that prints an integer with <code>"{:d}".format()</code>.</summary>
 <ul>
  <li>Prototype: <code>def safe_print_integer(value):</code></li>
  <li><code>value</code> can be any type (integer, string, etc.)</li>
  <li>The integer should be printed followed by a new line</li>
  <li>Returns <code>True</code> if <code>value</code> has been correctly printed (it means the value is an integer)</li>
  <li>Otherwise, returns <code>False</code></li>
  <li>You have to use <code>try:</code> / <code>except:</code></li>
  <li>You have to use <code>"{:d}".format()</code> to print as integer</li>
  <li>You are not allowed to import any module</li>
  <li>You are not allowed to use <code>type()</code></li>
 </ul>
</details>


<details>
 <summary> <code>2-safe_print_list_integers.py</code> - Write a function that prints the first x elements of a list and only integers.</summary>
 <ul>
  <li>Prototype: <code>def safe_print_list_integers(my_list=[], x=0):</code></li>
  <li><code>my_list</code> can contain any type (integer, string, etc.)</li>
  <li>All integers have to be printed on the same line followed by a new line - other types of values in the list must be skipped (in silence).</li>
  <li><code>x</code> represents the number of elements to access in <code>my_list</code></li>
  <li><code>x</code> can be bigger than the length of <code>my_list</code> - if it’s the case, an exception is expected to occur</li>
  <li>Returns the real number of integers printed</li>
  <li>You have to use <code>try:</code> / <code>except:</code></li>
  <li>You have to use <code>"{:d}".format()</code> to print an integer</li>
  <li>You are not allowed to import any module</li>
  <li>You are not allowed to use <code>len()</code></li>
 </ul>
</details>

<details>
 <summary> <code>3-safe_print_division.py</code> - Write a function that divides 2 integers and prints the result.</summary>
 <ul>
  <li>Prototype: <code>def safe_print_division(a, b):</code></li>
  <li>You can assume that <code>a</code> and <code>b</code> are integers</li>
  <li>The result of the division should print in the <code>finally:</code> section preceded by <code>Inside result:</code></li>
  <li>Returns the value of the division, otherwise: <code>None</code></li>
  <li>You have to use <code>try:</code> / <code>except:</code> / <code>finally:</code></li>
  <li>You have to use <code>"{}".format()</code> to print the result</li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

<details>
 <summary> <code>4-list_division.py</code> - Write a function that divides element by element 2 lists.</summary>
 <ul>
  <li>Prototype: <code>def list_division(my_list_1, my_list_2, list_length):</code></li>
  <li><code>my_list_1</code> and <code>my_list_2</code> can contain any type (integer, string, etc.)</li>
  <li><code>list_length</code> can be bigger than the length of both lists</li>
  <li>Returns a new list (length = <code>list_length</code>) with all divisions</li>
  <li>If 2 elements can’t be divided, the division result should be equal to 0</li>
  <li>If an element is not an integer or float:</li>
  <ul>
    <li>print: <code>wrong type</code></li>
  </ul>
  <li>If the division can’t be done (/0):</li>
  <ul>
    <li>print: <code>division by 0</code></li>
  </ul>
  <li>If <code>my_list_1</code> or <code>my_list_2</code> is too short:</li>
  <ul>
    <li>print: <code>out of range</code></li>
  </ul>
  <li>You have to use <code>try:</code> / <code>except:</code> / <code>finally:</code></li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

<details>
 <summary> <code>5-raise_exception.py</code> - Write a function that raises a type exception.</summary>
 <ul>
  <li>Prototype: <code>def raise_exception():</code></li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

<details>
 <summary> <code>6-raise_exception_msg.py</code> - Write a function that raises a name exception with a message.</summary>
 <ul>
  <li>Prototype: <code>def raise_exception_msg(message=""):</code></li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

## Advanced
<details>
 <summary> <code>7-safe_print_integer_err.py</code> - Write a function that prints an integer.</summary>
 <ul>
  <li>Prototype: <code>def safe_print_integer_err(value):</code></li>
  <li><code>value</code> can be any type (integer, string, etc.)</li>
  <li>The integer should be printed followed by a new line</li>
  <li>Returns <code>True</code> if <code>value</code> has been correctly printed (it means the value is an integer)</li>
  <li>Otherwise, returns <code>False</code> and prints in <code>stderr</code> the error preceded by <code>Exception:</code></li>
  <li>You have to use <code>try:</code> / <code>except:</code></li>
  <li>You have to use <code>"{:d}".format()</code> to print as an integer</li>
  <li>You are not allowed to use <code>type()</code></li>
 </ul>
</details>

<details>
 <summary> <code>8-safe_function.py</code> - Write a function that executes a function safely.</summary>
 <ul>
  <li>Prototype: <code>def safe_function(fct, *args):</code></li>
  <li>You can assume <code>fct</code> will always be a pointer to a function</li>
  <li>Returns the result of the function,</li>
  <li>Otherwise, returns <code>None</code> if something happens during the function and prints in <code>stderr</code> the error preceded by <code>Exception:</code></li>
  <li>You have to use <code>try:</code> / <code>except:</code></li>
 </ul>
</details>





