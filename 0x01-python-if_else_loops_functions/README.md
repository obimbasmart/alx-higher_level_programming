# Python - if/else, loops, functions





## Mandatory tasks

<details>
 <summary> <code>0-positive_or_negative.py</code> - This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print whether the number stored in the variable number is positive or negative.</summary>
 <ul>
  <li>You can find the source code <a href="https://intranet.alxswe.com/rltoken/e4tR3cjFHqhelf4y485-zQ">here</a></li>
   <li>The variable number will store a different value every time you will run this program</li>
    <li>You don’t have to understand what import, random. randint do. Please do not touch this code</li>
    <li>The output of the program should be:</li>
    <ul>
        <li>The number, followed by</li>
        <li>if the number is greater than 0: is positive</li>
        <li>if the number is 0: is zero</li>
        <li>if the number is less than 0: is negative</li>
        <li>followed by a new line</li>
    </ul>
 </ul>
</details>

<details>
 <summary> <code>1_last_digit.py</code> - This program will assign a random signed number to the variable <code>number</code> each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable <code>number</code>.</summary>
 <ul>
  <li>You can find the source code <a href="https://intranet.alxswe.com/rltoken/e4tR3cjFHqhelf4y485-zQ">here</a></li>
  <li>The variable <code>number</code> will store a different value every time you will run this program</li>
  <li>You don’t have to understand what <code>import</code>, <code>random.randint</code> do. Please do not touch this code. This line should not change: <code>number = random.randint(-10000, 10000)</code></li>
  <li>The output of the program should be:</li>
  <ul>
    <li>The string <code>Last digit of</code>, followed by</li>
    <li>the number, followed by</li>
    <li>the string <code>is</code>, followed by the last digit of <code>number</code>, followed by</li>
    <li>if the last digit is greater than 5: the string <code>and is greater than 5</code></li>
    <li>if the last digit is 0: the string <code>and is 0</code></li>
    <li>if the last digit is less than 6 and not 0: the string <code>and is less than 6 and not 0</code></li>
    <li>followed by a new line</li>
  </ul>
 </ul>
</details>

<details>
 <summary> <code>2-print_alphabet.py</code> - Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.</summary>
 <ul>
  <li>You can only use one <code>print</code> function with string format</li>
  <li>You can only use one loop in your code</li>
  <li>You are not allowed to store characters in a variable</li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

<details>
 <summary> <code>3-print_alphabet.py</code> - Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.</summary>
 <ul>
  <li>Print all the letters except q and e</li>
  <li>You can only use one <code>print</code> function with string format</li>
  <li>You can only use one loop in your code</li>
  <li>You are not allowed to store characters in a variable</li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>

<details>
 <summary> <code>print_hexa.py</code> - Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal (as in the following example)</summary>
 <ul>
  <li>You can only use one <code>print</code> function with string format</li>
  <li>You can only use one loop in your code</li>
  <li>You are not allowed to store numbers or strings in a variable</li>
  <li>You are not allowed to import any module</li>
 </ul>
</details>




## Advanced tasks
<details><summary><code>100-print_tebahpla.py</code> - Write a program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (`z` in lowercase and  `Y`  in uppercase) , not followed by a new line.</summary>
<ul>
<li> You can only use one  `print`  function with string format </li>
<li> You can only use one loop in your code </li>
 <li> You are not allowed to store characters in a variable</li>
<li> You are not allowed to import any module </li>
</ul>
</details>

<details>
 <summary> <code>101-remove_char_at.py</code> - Write a function that creates a copy of the string, removing the character at the position n (not the Python way, the “C array index”).</summary>
 <ul>
  <li>Prototype: <code>def remove_char_at(str, n):</code></li>
  <li>You are not allowed to import any module</li>
 </ul>
 You don’t need to understand <code>__import__</code>
</details>

<details>
 <summary> <code>102-magic_calculation.py</code>Write the Python function def magic_calculation(a, b, c): that does exactly the same as the following Python bytecode:</summary>
 <code>
  
     3          0 LOAD_FAST                0 (a)
                3 LOAD_FAST                1 (b)
                6 COMPARE_OP               0 (<)
                9 POP_JUMP_IF_FALSE       16
   
     4          12 LOAD_FAST                2 (c)
                15 RETURN_VALUE
   
     5     >>   16 LOAD_FAST                2 (c)
                19 LOAD_FAST                1 (b)
                22 COMPARE_OP               4 (>)
                25 POP_JUMP_IF_FALSE       36
   
     6          28 LOAD_FAST                0 (a)
                31 LOAD_FAST                1 (b)
                34 BINARY_ADD
                35 RETURN_VALUE
   
     7     >>   36 LOAD_FAST                0 (a)
                39 LOAD_FAST                1 (b)
                42 BINARY_MULTIPLY
                43 LOAD_FAST                2 (c)
                46 BINARY_SUBTRACT
                47 RETURN_VALUE
                
 </code>
</details>
