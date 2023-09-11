# Python - Everything is Object

In Python everything is an object, This project is an eye-opener on how Python treats mutable and non-mutable objects
> ## Key Learnings
> - Python classifies objects into two types: mutable and immutable.
> - Mutable objects include lists, while non-mutable objects encompass tuples, strings, integers, and more.
> - When passed to a function, Python handles mutable and non-mutable objects differently:
>   - Mutable objects are passed by reference, meaning changes made inside the function affect the object outside.
>   - Non-mutable objects are passed by value, creating a copy whenever passed to a function.
> - Python utilizes interning to optimize memory usage and performance for immutable objects like strings, integers, and small tuples:
>   - Interning applies to immutable objects, which cannot be altered once created.
>   - Common examples include small integers (-5 to 256), empty immutable sequences, and frequently used string literals.



#### Note:
All answers to the questions are located in the corresponding `.txt` file



## Mandatory
<details>
 <summary><code>0-answer.txt</code> - What function would you use to get the type of an object?</summary>
 <ul>
  <li><code>type()</code> - Write the name of the function in the file, without ()</li>
 </ul>
</details>

<details>
 <summary><code>1-answer.txt</code> - How do you get the variable identifier (which is the memory address in the CPython implementation)?</summary>
 <ul>
  <li>Write the name of the function in the file, without ()</li>
 </ul>
</details>

<details>
 <summary><code>2-answer.txt</code> - In the following code, do <code>a</code> and <code>b</code> point to the same object? Answer with Yes or No.</summary>
 <pre>
  >>> a = 89
  >>> b = 100
 </pre>
</details>

<details>
 <summary><code>3-answer.txt</code> - In the following code, do <code>a</code> and <code>b</code> point to the same object? Answer with Yes or No.</summary>
 <pre>
  >>> a = 89
  >>> b = 89
 </pre>
</details>

<details>
 <summary><code>4-answer.txt</code> - In the following code, do <code>a</code> and <code>b</code> point to the same object? Answer with Yes or No.</summary>
 <pre>
  >>> a = 89
  >>> b = a
 </pre>
</details>


<details>
 <summary><code>5-answer.txt</code> - In the following code, do a and b point to the same object? Answer with Yes or No.</summary>
 <pre>
    >>> a = 89
    >>> b = a + 1
    Yes
 </pre>
</details>

<details>
 <summary><code>6-answer.txt</code> - What do these 3 lines print?</summary>
 <pre>
    >>> s1 = "Best School"
    >>> s2 = s1
    >>> print(s1 == s2)
 </pre>
</details>

<details>
 <summary><code>7-answer.txt</code> - What do these 3 lines print?</summary>
 <pre>
    >>> s1 = "Best"
    >>> s2 = s1
    >>> print(s1 is s2)
 </pre>
</details>

<details>
 <summary><code>8-answer.txt</code> - What do these 3 lines print?</summary>
 <pre>
    >>> s1 = "Best School"
    >>> s2 = "Best School"
    >>> print(s1 == s2)
 </pre>
</details>

<details>
 <summary><code>9-answer.txt</code> - What do these 3 lines print?</summary>
 <pre>
    >>> s1 = "Best School"
    >>> s2 = "Best School"
    >>> print(s1 is s2)
 </pre>
</details>

<details>
 <summary><code>10-answer.txt</code> - What do these 3 lines print?</summary>
 <pre>
    >>> l1 = [1, 2, 3]
    >>> l2 = [1, 2, 3] 
    >>> print(l1 == l2)
 </pre>
</details>

<details>
 <summary><code>11-answer.txt</code> - What do these 3 lines print?</summary>
 <pre>
    >>> l1 = [1, 2, 3]
    >>> l2 = [1, 2, 3] 
    >>> print(l1 is l2)
 </pre>
</details>

<details>
 <summary><code>12-answer.txt</code> - What do these 3 lines print?</summary>
 <pre>
    >>> l1 = [1, 2, 3]
    >>> l2 = l1
    >>> print(l1 == l2)
 </pre>
</details>

<details>
 <summary><code>13-answer.txt</code> - What do these 3 lines print?</summary>
 <pre>
    >>> l1 = [1, 2, 3]
    >>> l2 = l1
    >>> print(l1 is l2)
 </pre>
</details>

<details>
 <summary><code>14-answer.txt</code> - What does this script print?</summary>
 <pre>
    l1 = [1, 2, 3]
    l2 = l1
    l1.append(4)
    print(l2)
 </pre>
</details>

<details>
 <summary><code>15-answer.txt</code> - What does this script print?</summary>
 <pre>
    l1 = [1, 2, 3]
    l2 = l1
    l1 = l1 + [4]
    print(l2)
 </pre>
</details>

<details>
 <summary><code>16-answer.txt</code> - What does this script print?</summary>
 <pre>
    def increment(n):
        n += 1

    a = 1
    increment(a)
    print(a)
 </pre>
</details>

<details>
 <summary><code>17-answer.txt</code> - What does this script print?</summary>
 <pre>
    def increment(n):
        n.append(4)

    l = [1, 2, 3]
    increment(l)
    print(l)
 </pre>
</details>

<details>
 <summary><code>18-answer.txt</code> - What does this script print?</summary>
 <pre>
    def assign_value(n, v):
        n = v

    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    assign_value(l1, l2)
    print(l1)
 </pre>
</details>

<details>
 <summary><code>19-copy_list.py</code> - Write a function def copy_list(l): that returns a copy of a list.</summary>
 <pre>
def copy_list(l):
    return l[:]
 </pre>
</details>

<details>
 <summary><code>20-answer.txt</code> - Is a a tuple? Answer with Yes or No.</summary>
 <pre>
    Yes
 </pre>
</details>

<details>
 <summary><code>21-answer.txt</code> - Is a a tuple? Answer with Yes or No.</summary>
 <pre>
    Yes
 </pre>
</details>

<details>
 <summary><code>22-answer.txt</code> - Is a a tuple? Answer with Yes or No.</summary>
 <pre>
    No
 </pre>
</details>

<details>
 <summary><code>23-answer.txt</code> - Is a a tuple? Answer with Yes or No.</summary>
 <pre>
    Yes
 </pre>
</details>

<details>
 <summary><code>24-answer.txt</code> - What does this script print?</summary>
 <pre>
    a = (1)
    b = (1)
    a is b
 </pre>
</details>

<details>
 <summary><code>25-answer.txt</code> - What does this script print?</summary>
 <pre>
    a = (1, 2)
    b = (1, 2)
    a is b
 </pre>
</details>

<details>
 <summary><code>26-answer.txt</code> - What does this script print?</summary>
 <pre>
    a = ()
    b = ()
    a is b
 </pre>
</details>

<details>
 <summary><code>27-answer.txt</code> - Will the last line of this script print 139926795932424? Answer with Yes or No.</summary>
 <pre>
    >>> id(a)
    139926795932424
    >>> a
    [1, 2, 3, 4]
    >>> a = a + [5]
    >>> id(a)
 </pre>
</details>

<details>
 <summary><code>28-answer.txt</code> - Will the last line of this script print 139926795932424? Answer with Yes or No.</summary>
 <pre>
    >>> a
    [1, 2, 3]
    >>> id (a)
    139926795932424
    >>> a += [4]
    >>> id(a)
 </pre>
</details>


## Advanced

1- Write a class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name.

- You are not allowed to import any module
