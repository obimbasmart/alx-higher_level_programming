# Python - Input/Output

> In this project, I gained valuable insights into file manipulation in Python, specifically focusing on reading and writing files. Additionally, I delved into the significance and utilization of JSON (JavaScript Object Notation) for serializing and deserializing data objects.

> Before this project, I commonly associated JSON with the name "Jason," but I've come to understand that JSON stands for JavaScript Object Notation. JSON is essentially a dictionary-like representation of an object, and it extends beyond Python, having its roots in the JavaScript programming language. It serves as a universally accepted format for exchanging data objects across different platforms, enhancing interoperability.

# Mandatory

<details>
  <summary>
    <code>0-read_file.py</code> - Write a function that reads a text file (UTF8) and prints it to stdout.
  </summary>
  <ul>
    <li>Prototype: <code>def read_file(filename="")</code></li>
    <li>You must use the with statement</li>
    <li>You don’t need to manage file permission or file doesn't exist exceptions.</li>
    <li>You are not allowed to import any module</li>
    <li>Example Usage provided</li>
  </ul>
</details>

<details>
  <summary>
    <code>1-write_file.py</code> - Write a function that writes a string to a text file (UTF8) and returns the number of characters written.
  </summary>
  <ul>
    <li>Prototype: <code>def write_file(filename="", text="")</code></li>
    <li>You must use the with statement</li>
    <li>You don’t need to manage file permission exceptions.</li>
    <li>Your function should create the file if it doesn’t exist.</li>
    <li>Your function should overwrite the content of the file if it already exists.</li>
    <li>You are not allowed to import any module</li>
    <li>Example Usage provided</li>
  </ul>
</details>

<details>
  <summary>
    <code>2-append_write.py</code> - Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added.
  </summary>
  <ul>
    <li>Prototype: <code>def append_write(filename="", text="")</code></li>
    <li>If the file doesn’t exist, it should be created</li>
    <li>You must use the with statement</li>
    <li>You don’t need to manage file permission or file doesn't exist exceptions.</li>
    <li>You are not allowed to import any module</li>
    <li>Example Usage provided</li>
  </ul>
</details>

<details>
  <summary>
    <code>3-to_json_string.py</code> - Write a function that returns the JSON representation of an object (string).
  </summary>
  <ul>
    <li>Prototype: <code>def to_json_string(my_obj)</code></li>
    <li>You don’t need to manage exceptions if the object can’t be serialized.</li>
    <li>Example Usage provided</li>
  </ul>
</details>

<details>
  <summary>
    <code>4-from_json_string.py</code> - Write a function that returns an object (Python data structure) represented by a JSON string.
  </summary>
  <ul>
    <li>Prototype: <code>def from_json_string(my_str)</code></li>
    <li>You don’t need to manage exceptions if the JSON string doesn’t represent an object.</li>
    <li>Example Usage provided</li>
  </ul>
</details>

<details>
  <summary>
    <code>5-save_to_json_file.py</code> - Write a function that writes an Object to a text file, using a JSON representation.
  </summary>
  <ul>
    <li>Prototype: <code>def save_to_json_file(my_obj, filename)</code></li>
    <li>You must use the with statement</li>
    <li>You don’t need to manage exceptions if the object can’t be serialized.</li>
    <li>You don’t need to manage file permission exceptions.</li>
    <li>Example Usage provided</li>
  </ul>
</details>

<details>
  <summary>
    <code>6-load_from_json_file.py</code> - Write a function that creates an Object from a “JSON file”.
  </summary>
  <ul>
    <li>Prototype: <code>def load_from_json_file(filename)</code></li>
    <li>You must use the with statement</li>
    <li>You don’t need to manage exceptions if the JSON string doesn’t represent an object.</li>
    <li>You don’t need to manage file permissions / exceptions.</li>
    <li>Example Usage provided</li>
  </ul>
</details>

<details>
  <summary>
    <code>7-add_item.py</code> - Write a script that adds all arguments to a Python list, and then save them to a file.
  </summary>
  <ul>
    <li>You must use your function <code>save_to_json_file</code> from <code>5-save_to_json_file.py</code></li>
    <li>You must use your function <code>load_from_json_file</code> from <code>6-load_from_json_file.py</code></li>
    <li>The list must be saved as a JSON representation in a file named <code>add_item.json</code></li>
    <li>If the file doesn’t exist, it should be created</li>
    <li>You don’t need to manage file permissions / exceptions.</li>
    <li>Example Usage provided</li>
  </ul>
</details>

<details>
  <summary>
    <code>8-class_to_json.py</code> - Write a function that returns the dictionary description with a simple data structure (list, dictionary, string, integer, and boolean) for JSON serialization of an object.
  </summary>
  <ul>
    <li>Prototype: <code>def class_to_json(obj)</code></li>
    <li><code>obj</code> is an instance of a Class</li>
    <li>All attributes of the <code>obj</code> Class are serializable: list, dictionary, string, integer, and boolean</li>
    <li>You are not allowed to import any module</li>
    <li>Example Usage provided</li>
  </ul>
</details>

<details>
  <summary>
    <code>9-student.py</code> - Write a class Student that defines a student by:
  </summary>
  <ul>
    <li>Public instance attributes: first_name, last_name, age</li>
    <li>Instantiation with first_name, last_name, and age: <code>def __init__(self, first_name, last_name, age)</code></li>
    <li>Public method <code>def to_json(self)</code> that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py)</li>
    <li>You are not allowed to import any module</li>
    <li>Example Usage provided</li>
  </ul>
</details>

<details>
  <summary>
    <code>10-student.py</code> - Write a class Student that defines a student by: (based on 9-student.py)
  </summary>
  <ul>
    <li>Public instance attributes: first_name, last_name, age</li>
    <li>Instantiation with first_name, last_name, and age: <code>def __init__(self, first_name, last_name, age)</code></li>
    <li>Public method <code>def to_json(self, attrs=None)</code> that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
      <ul>
        <li>If <code>attrs</code> is a list of strings, only attribute names contained in this list must be retrieved.</li>
        <li>Otherwise, all attributes must be retrieved</li>
      </ul>
    </li>
    <li>You are not allowed to import any module</li>
    <li>Example Usage provided</li>
  </ul>
</details>

<details>
  <summary>
    <code>11-student.py</code> - Write a class Student that defines a student by: (based on 10-student.py)
  </summary>
  <ul>
    <li>Public instance attributes: first_name, last_name, age</li>
    <li>Instantiation with first_name, last_name, and age: <code>def __init__(self, first_name, last_name, age)</code></li>
    <li>Public method <code>def to_json(self, attrs=None)</code> that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
      <ul>
        <li>If <code>attrs</code> is a list of strings, only attribute names contained in this list must be retrieved.</li>
        <li>Otherwise, all attributes must be retrieved</li>
      </ul>
    </li>
    <li>Public method <code>def reload_from_json(self, json)</code> that replaces all attributes of the Student instance:
      <ul>
        <li>You can assume json will always be a dictionary</li>
        <li>A dictionary key will be the public attribute name</li>
        <li>A dictionary value will be the value of the public attribute</li>
      </ul>
    </li>
    <li>You are not allowed to import any module</li>
    <li>Example Usage provided</li>
  </ul>
</details>

<details>
  <summary>
    <code>12-pascal_triangle.py</code> - Create a function <code>def pascal_triangle(n)</code> that returns a list of lists of integers representing Pascal's triangle of <code>n</code>:
  </summary>
  <ul>
    <li>Returns an empty list if <code>n <= 0</code></li>
    <li>You can assume <code>n</code> will always be an integer</li>
    <li>You are not allowed to import any module</li>
    <li>Example Usage provided</li>
  </ul>
</details>

## Advanced

<details>
  <summary>
    <code>100-append_after.py</code> - Write a function that inserts a line of text into a file, after each line containing a specific string (see example):
  </summary>
  <ul>
    <li>Prototype: <code>def append_after(filename="", search_string="", new_string="")</code></li>
    <li>You must use the with statement</li>
    <li>You don’t need to manage file permission or file doesn't exist exceptions.</li>
    <li>You are not allowed to import any module</li>
    <li>Example Usage provided</li>
  </ul>
</details>




