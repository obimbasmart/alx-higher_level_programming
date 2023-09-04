# Python - Test-driven development
> In this Python project, I explored the world of testing (Doctest and Unittest) to ensure code is rock-solid and dependable. Never trust the user; ensure comprehensive testing to guarantee the reliability of software. In conclusion, **TRUST, BUT VERIFY** by testing.



**Note**: All test files for each task are located inside the `test/` directory
## Mandatory
<details>
 <summary> <code>0-add_integer.py</code> - Write a function that adds 2 integers.</summary>
 <ul>
  <li>Prototype: <code>def add_integer(a, b=98):</code></li>
  <li><code>a</code> and <code>b</code> must be integers or floats, otherwise raise a <code>TypeError</code> exception with the message <code>a must be an integer or b must be an integer</code></li>
  <li><code>a</code> and <code>b</code> must be first casted to integers if they are float</li>
  <li>Returns an integer: the addition of <code>a</code> and <code>b</code></li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

<details>
 <summary> <code>2-matrix_divided.py</code> - Write a function that divides all elements of a matrix.</summary>
 <ul>
  <li>Prototype: <code>def matrix_divided(matrix, div):</code></li>
  <li><code>matrix</code> must be a list of lists of integers or floats, otherwise raise a <code>TypeError</code> exception with the message <code>matrix must be a matrix (list of lists) of integers/floats</code></li>
  <li>Each row of the matrix must be of the same size, otherwise raise a <code>TypeError</code> exception with the message <code>Each row of the matrix must have the same size</code></li>
  <li><code>div</code> must be a number (integer or float), otherwise raise a <code>TypeError</code> exception with the message <code>div must be a number</code></li>
  <li><code>div</code> can’t be equal to 0, otherwise raise a <code>ZeroDivisionError</code> exception with the message <code>division by zero</code></li>
  <li>All elements of the matrix should be divided by <code>div</code>, rounded to 2 decimal places</li>
  <li>Returns a new matrix</li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

<details>
 <summary> <code>3-say_my_name.py</code> - Write a function that prints My name is &lt;first name&gt; &lt;last name&gt;</summary>
 <ul>
  <li>Prototype: <code>def say_my_name(first_name, last_name=""):</code></li>
  <li><code>first_name</code> and <code>last_name</code> must be strings, otherwise raise a <code>TypeError</code> exception with the message <code>first_name must be a string or last_name must be a string</code></li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

<details>
 <summary> <code>4-print_square.py</code> - Write a function that prints a square with the character #.</summary>
 <ul>
  <li>Prototype: <code>def print_square(size):</code></li>
  <li><code>size</code> is the size length of the square</li>
  <li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code></li>
  <li>If <code>size</code> is less than 0, raise a <code>ValueError</code> exception with the message <code>size must be >= 0</code></li>
  <li>If <code>size</code> is a float and is less than 0, raise a <code>TypeError</code> exception with the message <code>size must be an integer</code></li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

<details>
 <summary> <code>5-text_indentation.py</code> - Write a function that prints a text with 2 new lines after each of these characters: ., ? and :</summary>
 <ul>
  <li>Prototype: <code>def text_indentation(text):</code></li>
  <li><code>text</code> must be a string, otherwise raise a <code>TypeError</code> exception with the message <code>text must be a string</code></li>
  <li>There should be no space at the beginning or at the end of each printed line</li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

<details>
  <summary><code>6-max_integer_test.py</code> Unit test the function: <code>6-max_integer.py</code></summary>
  <ul>
    <li>In this task, you will write unittests for the function below: <code>6-max_integer.py</code>.</li>
    <li>Your test file should be inside a folder <code>tests</code>.</li>
    <li>You have to use the <code>unittest</code> module.</li>
    <li>Your test file should be python files (extension: <code>.py</code>).</li>
    <li>Your test file should be executed by using this command: <code>python3 -m unittest tests.6-max_integer_test</code>.</li>
    <li>All tests you make must be passable by the function below.</li>
    <li>We strongly encourage you to work together on test cases so that you don’t miss any edge cases.</li>
  </ul>
</details>



## Advanced

<details><summary><code>100-matrix_mul.py</code> - Write a function that multiplies two matrix:</summary>
  <ul>
    <li>Function Prototype: <code>def matrix_mul(m_a, m_b):</code></li>
    <li><strong>Validation Requirements:</strong>
      <ol>
        <li><code>m_a</code> and <code>m_b</code> must be a list of lists of integers or floats:</li>
        <ul>
          <li>If <code>m_a</code> or <code>m_b</code> is not a list, raise a <code>TypeError</code> exception with the message <code>m_a must be a list or m_b must be a list</code>.</li>
          <li>If <code>m_a</code> or <code>m_b</code> is not a list of lists, raise a <code>TypeError</code> exception with the message <code>m_a must be a list of lists or m_b must be a list of lists</code>.</li>
        </ul>
        <li>If <code>m_a</code> or <code>m_b</code> is empty (i.e., <code>[]</code> or <code>[[]]</code>), raise a <code>ValueError</code> exception with the message <code>m_a can't be empty or m_b can't be empty</code>.</li>
        <li>If one element of those list of lists is not an integer or a float, raise a <code>TypeError</code> exception with the message <code>m_a should contain only integers or floats or m_b should contain only integers or floats</code>.</li>
        <li>If <code>m_a</code> or <code>m_b</code> is not a rectangle (all ‘rows’ should be of the same size), raise a <code>TypeError</code> exception with the message <code>each row of m_a must be of the same size or each row of m_b must be of the same size</code>.</li>
      </ol>
    </li>
    <li>If <code>m_a</code> and <code>m_b</code> can’t be multiplied, raise a <code>ValueError</code> exception with the message <code>m_a and m_b can't be multiplied</code>.</li>
    <li>You are not allowed to import any module.</li>
  </ul>
</details>




