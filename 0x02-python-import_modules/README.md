# Python - import & modules


## Mandatory tasks
<details>
 <summary> <code>0-add.py</code> - Write a program that imports the function <code>def add(a, b):</code> from the file <code>add_0.py</code> and prints the result of the addition <code>1 + 2 = 3</code></summary>
 <ul>
  <li>You have to use <code>print</code> function with string format to display integers</li>
  <li>You have to assign:</li>
  <ul>
   <li>the value <code>1</code> to a variable called <code>a</code></li>
   <li>the value <code>2</code> to a variable called <code>b</code></li>
  </ul>
  <li>and use those two variables as arguments when calling the functions <code>add</code> and <code>print</code></li>
  <li><code>a</code> and <code>b</code> must be defined in 2 different lines: <code>a = 1</code> and another <code>b = 2</code></li>
  <li>Your program should print: <code>&lt;a value&gt; + &lt;b value&gt; = &lt;add(a, b) value&gt;</code> followed with a new line</li>
  <li>You can only use the word <code>add_0</code> once in your code</li>
  <li>You are not allowed to use <code>*</code> for importing or <code>__import__</code></li>
  <li>Your code should not be executed when imported - by using <code>__import__</code>, like the example below</li>
 </ul>
</details>

<details>
 <summary> <code>1-calculation.py</code> - Write a program that imports functions from the file <code>calculator_1.py</code>, does some Maths, and prints the result.</summary>
 <ul>
  <li>Do not use the function <code>print</code> (with string format to display integers) more than 4 times</li>
  <li>You have to define:</li>
  <ul>
   <li>the value <code>10</code> to a variable <code>a</code></li>
   <li>the value <code>5</code> to a variable <code>b</code></li>
  </ul>
  <li>and use those two variables only, as arguments when calling functions (including <code>print</code>)</li>
  <li><code>a</code> and <code>b</code> must be defined in 2 different lines: <code>a = 10</code> and another <code>b = 5</code></li>
  <li>Your program should call each of the imported functions. See example below for format</li>
  <li>the word <code>calculator_1</code> should be used only once in your file</li>
  <li>You are not allowed to use <code>*</code> for importing or <code>__import__</code></li>
  <li>Your code should not be executed when imported</li>
 </ul>
</details>

<details>
 <summary> <code>2-args.py</code> - Write a program that prints the number of and the list of its arguments.</summary>
 <ul>
  <li>The output should be:</li>
  <ul>
   <li>Number of argument(s) followed by <code>argument</code> (if number is one) or <code>arguments</code> (otherwise), followed by</li>
   <li>: (or . if no arguments were passed) followed by</li>
   <li>a new line, followed by (if at least one argument),</li>
   <li>one line per argument:</li>
   <ul>
    <li>the position of the argument (starting at 1) followed by <code>:</code>, followed by the argument value and a new line</li>
   </ul>
  </ul>
  <li>Your code should not be executed when imported</li>
  <li>The number of elements of <code>argv</code> can be retrieved by using: <code>len(argv)</code></li>
  <li>You do not have to fully understand lists yet, but imagine that <code>argv</code> can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.</li>
 </ul>
</details>

<details>
 <summary> <code>3-infinit_ad.py</code> - Write a program that prints the result of the addition of all arguments.</summary>
 <ul>
  <li>The output should be the result of the addition of all arguments, followed by a new line</li>
  <li>You can cast arguments into integers by using <code>int()</code> (you can assume that all arguments can be casted into integers)</li>
  <li>Your code should not be executed when imported</li>
 </ul>
</details>

<details>
 <summary> <code>4-hidden_discovery.py</code> - Write a program that prints all the names defined by the compiled module <code>hidden_4.pyc</code> (please download it locally).</summary>
 <ul>
  <li>You should print one name per line, in alpha order</li>
  <li>You should print only names that do not start with <code>__</code></li>
  <li>Your code should not be executed when imported</li>
  <li>Make sure you are running your code in Python 3.8.x (<code>hidden_4.pyc</code> has been compiled with this version)</li>
 </ul>
 <p>Download <code>hidden_4.pyc</code> from: <a href="https://github.com/alx-tools/0x02.py/raw/master/hidden_4.pyc">hidden_4.pyc</a></p>
</details>

<details>
 <summary> <code>5-variable_load.py</code> - Write a program that imports the variable <code>a</code> from the file <code>variable_load_5.py</code> and prints its value.</summary>
 <ul>
  <li>You are not allowed to use <code>*</code> for importing or <code>__import__</code></li>
  <li>Your code should not be executed when imported</li>
 </ul>
</details>


## Advanced tasks
<details>
 <summary> <code>100-my_calculator.py</code> - Write a program that imports all functions from the file <code>calculator_1.py</code> and handles basic operations.</summary>
 <ul>
  <li>Usage: <code>./100-my_calculator.py a operator b</code></li>
  <li>If the number of arguments is not 3, your program has to:</li>
  <ul>
   <li>print <code>Usage: ./100-my_calculator.py &lt;a&gt; &lt;operator&gt; &lt;b&gt;</code> followed with a new line</li>
   <li>exit with the value 1</li>
  </ul>
  <li>operator can be:</li>
  <ul>
   <li><code>+</code> for addition</li>
   <li><code>-</code> for subtraction</li>
   <li><code>*</code> for multiplication</li>
   <li><code>/</code> for division</li>
  </ul>
  <li>If the operator is not one of the above:</li>
  <ul>
   <li>print <code>Unknown operator. Available operators: +, -, * and /</code> followed with a new line</li>
   <li>exit with the value 1</li>
  </ul>
  <li>You can cast <code>a</code> and <code>b</code> into integers by using <code>int()</code> (you can assume that all arguments will be castable into integers)</li>
  <li>The result should be printed like this: <code>&lt;a&gt; &lt;operator&gt; &lt;b&gt; = &lt;result&gt;</code>, followed by a new line</li>
  <li>You are not allowed to use <code>*</code> for importing or <code>__import__</code></li>
  <li>Your code should not be executed when imported</li>
 </ul>
</details>

<details>
 <summary> <code>101-easy_print.py</code> - Write a program that prints <code>#pythoniscool</code>, followed by a new line, in the standard output.</summary>
 <ul>
  <li>Your program should be maximum 2 lines long</li>
  <li>You are not allowed to use <code>print</code> or <code>eval</code> or <code>open</code> or <code>import sys</code> in your file <code>101-easy_print.py</code></li>
 </ul>
</details>

<details>
 <summary> <code>magic_calculation.py</code> - Write the Python function <code>def magic_calculation(a, b)</code> that does exactly the same as the following Python bytecode:</summary>
 <code style="background-color: red">
   
     3          0 LOAD_CONST              1 (0)
                3 LOAD_CONST               2 (('add', 'sub'))
                6 IMPORT_NAME              0 (magic_calculation_102)
                9 IMPORT_FROM              1 (add)
               12 STORE_FAST               2 (add)
               15 IMPORT_FROM              2 (sub)
               18 STORE_FAST               3 (sub)
               21 POP_TOP

    4          22 LOAD_FAST                0 (a)
               25 LOAD_FAST                1 (b)
               28 COMPARE_OP               0 (&lt;)
               31 POP_JUMP_IF_FALSE       94

    5          34 LOAD_FAST                2 (add)
               37 LOAD_FAST                0 (a)
               40 LOAD_FAST                1 (b)
               43 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
               46 STORE_FAST               4 (c)

    6          49 SETUP_LOOP               38 (to 90)
               52 LOAD_GLOBAL              3 (range)
               55 LOAD_CONST               3 (4)
               58 LOAD_CONST               4 (6)
               61 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
               64 GET_ITER
               65 FOR_ITER                 21 (to 89)
               68 STORE_FAST               5 (i)

    7          71 LOAD_FAST                2 (add)
               74 LOAD_FAST                4 (c)
               77 LOAD_FAST                5 (i)
               80 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
               83 STORE_FAST               4 (c)
               86 JUMP_ABSOLUTE           65
               9 POP_BLOCK

    8          90 LOAD_FAST                4 (c)
               93 RETURN_VALUE
               
    10         94 LOAD_FAST                3 (sub)
               97 LOAD_FAST                0 (a)
              100 LOAD_FAST                1 (b)
              103 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
              106 RETURN_VALUE
              107 LOAD_CONST               0 (None)
              110 RETURN_VALUE
          
 </code>
 
 <p>Tip: <a href="https://intranet.alxswe.com/rltoken/FMdg7W8NKJZKRuFGG8mzmg">Python bytecode</a></p>
</details>

