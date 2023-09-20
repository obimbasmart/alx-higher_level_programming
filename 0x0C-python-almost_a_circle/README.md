# Python - Almost a Circle


> This project was fun and very hands-on. I utilized various concepts learned  in previous projects:
 - > - Import - Exceptions - Class - Private attribute
    - `Getter/Sette` - `Class method` - `Static method` - `Inheritance`
    - `Unittest` - `Read/Write file`

> The project revolved around creating a versatile "Geometry" class hierarchy, starting with a foundational base class. While `Base` may not correspond to a real-world shape, it served as the blueprint for all geometric entities (e.g., Rectangle, Square, Circle). This approach minimized redundancy and maximized code reusability.

> Moreover, I delved into the intricacies of serializing and deserializing classes, enabling me to store and retrieve objects effortlessly from `JSON` files. It was a fascinating learning experience.

> As a firm believer in the adage, `"If it's not tested, it doesn't work,"` I meticulously crafted a suite of unit tests, residing in the dedicated "test" folder, to ensure the robustness of my code.

> To top it all off, I embarked on an entertaining adventure, employing Python's "turtle" module to visually render each geometric shape on the screen. Witnessing these objects come to life through code was an absolute delight.

> This project was an engaging blend of theory and hands-on practice, allowing me to consolidate my knowledge while having a great time in the process.


## Mandatory tasks

<details>
  <summary>
    <code>models/base.py</code> - Write the first class <code>Base</code>:
  </summary>
  <ul>
    <li>Create a folder named <code>models</code> with an empty file <code>__init__.py</code> inside - with this file, the folder will become a Python package</li>
    <li>Create a file named <code>models/base.py</code>:</li>
    <ul>
      <li>Class <code>Base</code>:</li>
      <ul>
        <li>Private class attribute <code>__nb_objects = 0</code></li>
        <li>Class constructor: <code>def __init__(self, id=None)</code></li>
        <ul>
          <li>If <code>id</code> is not None, assign the public instance attribute <code>id</code> with this argument value - you can assume <code>id</code> is an integer and you don't need to test its type</li>
          <li>Otherwise, increment <code>__nb_objects</code> and assign the new value to the public instance attribute <code>id</code></li>
        </ul>
        <li>This class will be the "base" of all other classes in this project. The goal of it is to manage the <code>id</code> attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)</li>
      </ul>
    </ul>
  </ul>
</details>

<details>
  <summary>
    <code>models/rectangle.py</code> - Write the class <code>Rectangle</code> that inherits from <code>Base</code>:
  </summary>
  <ul>
    <li>Class <code>Rectangle</code> inherits from <code>Base</code></li>
    <li>Private instance attributes, each with its own public getter and setter:</li>
    <ul>
      <li><code>__width</code> -> <code>width</code></li>
      <li><code>__height</code> -> <code>height</code></li>
      <li><code>__x</code> -> <code>x</code></li>
      <li><code>__y</code> -> <code>y</code></li>
    </ul>
    <li>Class constructor: <code>def __init__(self, width, height, x=0, y=0, id=None):</code></li>
    <ul>
      <li>Call the super class with <code>id</code> - this super call will use the logic of the <code>__init__</code> of the <code>Base</code> class</li>
      <li>Assign each argument <code>width</code>, <code>height</code>, <code>x</code>, and <code>y</code> to the right attribute</li>
    </ul>
    <li>Why private attributes with getter/setter? Why not directly public attribute?</li>
    <ul>
      <li>Because we want to protect attributes of our class. With a setter, you are able to validate what a developer is trying to assign to a variable. So after, in your class, you can "trust" these attributes.</li>
    </ul>
  </ul>
</details>

<details>
  <summary>
    <code>models/rectangle.py</code> - Validate attributes
  </summary>
  <ul>
    <li>Update the class <code>Rectangle</code> by adding validation of all setter methods and instantiation (id excluded):</li>
    <ul>
      <li>If the input is not an integer, raise the <code>TypeError</code> exception with the message: <code>&lt;name of the attribute&gt; must be an integer.</code> Example: <code>width must be an integer</code></li>
      <li>If <code>width</code> or <code>height</code> is under or equals 0, raise the <code>ValueError</code> exception with the message: <code>&lt;name of the attribute&gt; must be &gt; 0.</code> Example: <code>width must be &gt; 0</code></li>
      <li>If <code>x</code> or <code>y</code> is under 0, raise the <code>ValueError</code> exception with the message: <code>&lt;name of the attribute&gt; must be &gt;= 0.</code> Example: <code>x must be &gt;= 0</code></li>
    </ul>
    <li>Example Usage provided</li>
  </ul>
</details>


<details>
  <summary>
    <code>models/rectangle.py</code> - Update the class <code>Rectangle</code> by adding the public method <code>def area(self)</code> that returns the area value of the <code>Rectangle</code> instance.
  </summary>
</details>

<details>
  <summary>
    <code>models/rectangle.py</code> - Update the class <code>Rectangle</code> by adding the public method <code>def display(self)</code> that prints in stdout the <code>Rectangle</code> instance with the character # - you don’t need to handle x and y here.
  </summary>
</details>

<details>
  <summary>
    <code>models/rectangle.py</code> - Update the class <code>Rectangle</code> by overriding the <code>__str__</code> method so that it returns <code>[Rectangle] (&lt;id&gt;) &lt;x&gt;/&lt;y&gt; - &lt;width&gt;/&lt;height&gt;</code>
  </summary>
</details>

<details>
  <summary>
    <code>models/rectangle.py</code> - Update the class <code>Rectangle</code> by improving the public method <code>def display(self)</code> to print in stdout the Rectangle instance with the character # by taking care of x and y
  </summary>
</details>

<details>
  <summary>
    <code>models/rectangle.py</code> - Update the class <code>Rectangle</code> by adding the public method <code>def update(self, *args)</code> that assigns an argument to each attribute:
  </summary>
  <ul>
    <li>1st argument should be the id attribute</li>
    <li>2nd argument should be the width attribute</li>
    <li>3rd argument should be the height attribute</li>
    <li>4th argument should be the x attribute</li>
    <li>5th argument should be the y attribute</li>
    <li>This type of argument is called a “no-keyword argument” - Argument order is super important.</li>
  </ul>
</details>

<details>
  <summary>
    <code>models/rectangle.py</code> - Update the class <code>Rectangle</code> by updating the public method <code>def update(self, *args)</code> to <code>def update(self, *args, **kwargs)</code> that assigns key/value arguments to attributes:
  </summary>
  <ul>
    <li><code>**kwargs</code> can be thought of as a double pointer to a dictionary: key/value</li>
    <li>As Python doesn’t have pointers, <code>**kwargs</code> is not literally a double pointer – describing it as such is just a way of explaining its behavior in terms you’re already familiar with</li>
    <li><code>**kwargs</code> must be skipped if <code>*args</code> exists and is not empty</li>
    <li>Each key in this dictionary represents an attribute of the instance</li>
    <li>This type of argument is called a “key-worded argument”. Argument order is not important.</li>
  </ul>
</details>

<details>
  <summary>
    <code>models/square.py</code> - Write the class <code>Square</code> that inherits from <code>Rectangle</code>:
  </summary>
  <ul>
    <li>Class <code>Square</code> inherits from <code>Rectangle</code></li>
    <li>Class constructor: <code>def __init__(self, size, x=0, y=0, id=None)</code>:
      <ul>
        <li>Call the super class with <code>id</code>, <code>x</code>, <code>y</code>, <code>width</code>, and <code>height</code> - this super call will use the logic of the <code>__init__</code> of the <code>Rectangle</code> class.</li>
        <li>The <code>width</code> and <code>height</code> must be assigned to the value of <code>size</code></li>
      </ul>
    </li>
    <li>You must not create new attributes for this class, use all attributes of <code>Rectangle</code> - As a reminder: a <code>Square</code> is a <code>Rectangle</code> with the same <code>width</code> and <code>height</code></li>
    <li>All <code>width</code>, <code>height</code>, <code>x</code>, and <code>y</code> validation must inherit from <code>Rectangle</code> - same behavior in case of wrong data</li>
    <li>The overloading <code>__str__</code> method should return <code>[Square] (<id>) <x>/<y> - <size></code> - in our case, <code>width</code> or <code>height</code></li>
    <li>As you know, a <code>Square</code> is a special <code>Rectangle</code>, so it makes sense this class <code>Square</code> inherits from <code>Rectangle</code>. Now you have a <code>Square</code> class that has the same attributes and same methods.</li>
  </ul>
</details>

<details>
  <summary>
    <code>models/square.py</code> - Update the class <code>Square</code> by adding the public getter and setter <code>size</code>:
  </summary>
  <ul>
    <li>The setter should assign (in this order) the <code>width</code> and the <code>height</code> - with the same value</li>
    <li>The setter should have the same value validation as the <code>Rectangle</code> for <code>width</code> and <code>height</code> - No need to change the exception error message (It should be the one from <code>width</code>)</li>
  </ul>
</details>


<details>
  <summary>
    <code>models/square.py</code> - Update the class <code>Square</code> by adding the public method <code>def update(self, *args, **kwargs)</code> that assigns attributes:
  </summary>
  <ul>
    <li><code>*args</code> is the list of arguments - no-keyworded arguments</li>
    <li>1st argument should be the <code>id</code> attribute</li>
    <li>2nd argument should be the <code>size</code> attribute</li>
    <li>3rd argument should be the <code>x</code> attribute</li>
    <li>4th argument should be the <code>y</code> attribute</li>
    <li><code>**kwargs</code> can be thought of as a double pointer to a dictionary: key/value (keyworded arguments)</li>
    <li><code>**kwargs</code> must be skipped if <code>*args</code> exists and is not empty</li>
    <li>Each key in this dictionary represents an attribute to the instance</li>
  </ul>
</details>


<details>
  <summary>
    <code>models/rectangle.py</code> - Update the class <code>Rectangle</code> by adding the public method <code>def to_dictionary(self)</code> that returns the dictionary representation of a Rectangle:
  </summary>
  <ul>
    <li>This dictionary must contain:</li>
    <ul>
      <li>id</li>
      <li>width</li>
      <li>height</li>
      <li>x</li>
      <li>y</li>
    </ul>
  </ul>
</details>

<details>
  <summary>
    <code>models/square.py</code> - Update the class Square by adding the public method <code>def to_dictionary(self)</code> that returns the dictionary representation of a Square:
  </summary>
  <p>This dictionary must contain:</p>
  <ul>
    <li>id</li>
    <li>size</li>
    <li>x</li>
    <li>y</li>
  </ul>
</details>

<details>
  <summary>
    <code>models/base.py</code> - Update the class Base by adding the static method <code>def to_json_string(list_dictionaries)</code> that returns the JSON string representation of list_dictionaries:
  </summary>
  <p>This method should have the following behavior:</p>
  <ul>
    <li>list_dictionaries is a list of dictionaries</li>
    <li>If list_dictionaries is None or empty, return the string: "[]"</li>
    <li>Otherwise, return the JSON string representation of list_dictionaries</li>
  </ul>
</details>

<details>
  <summary>
    <code>models/base.py</code> - Update the class Base by adding the class method <code>def save_to_file(cls, list_objs)</code> that writes the JSON string representation of list_objs to a file:
  </summary>
  <p>This method should have the following behavior:</p>
  <ul>
    <li>list_objs is a list of instances who inherits of Base - example: list of Rectangle or list of Square instances</li>
    <li>If list_objs is None, save an empty list</li>
    <li>The filename must be: &lt;Class name&gt;.json - example: Rectangle.json</li>
    <li>You must use the static method to_json_string (created before)</li>
    <li>You must overwrite the file if it already exists</li>
  </ul>
</details>


<details>
  <summary>
    <code>models/base.py</code> - Update the class Base by adding the class method <code>def create(cls, **dictionary)</code> that returns an instance with all attributes already set:
  </summary>
  <p>This method should have the following behavior:
  <ul>
    <li>dictionary can be thought of as a double pointer to a dictionary.
    <li>To use the update method to assign all attributes, you must create a “dummy” instance before:</li>
    <ul>
      <li>Create a Rectangle or Square instance with “dummy” mandatory attributes (width, height, size, etc.)</li>
      <li>Call the update instance method on this “dummy” instance to apply your real values</li>
    </ul>
    <li>You must use the method def update(self, *args, **kwargs)</li>
    <li>dictionary must be used as **kwargs of the method update</li>
    <li>You are not allowed to use eval</li>
  </ul>
</details>


<details>
  <summary>
    <code>models/base.py</code> - Update the class Base by adding the class method <code>def load_from_file(cls)</code> that returns a list of instances:
  </summary>
  <p>This method should have the following behavior:</p>
  <ul>
    <li>The filename must be: <code>&lt;Class name&gt;.json</code> - example: <code>Rectangle.json</code></li>
    <li>If the file doesn’t exist, return an empty list</li>
    <li>Otherwise, return a list of instances - the type of these instances depends on cls (current class using this method)</li>
    <li>You must use the <code>from_json_string</code> and <code>create</code> methods (implemented previously)</li>
  </ul>
</details>


## Advanced tasks

<details>
  <summary>
    <code>models/base.py</code> - Update the class Base by adding the class methods <code>def save_to_file_csv(cls, list_objs)</code> and <code>def load_from_file_csv(cls)</code> that serializes and deserializes in CSV:
  </summary>
  <p>These methods should have the following behavior:</p>
  <ul>
    <li>The filename must be: <code>&lt;Class name&gt;.csv</code> - example: <code>Rectangle.csv</code></li>
    <li>Has the same behavior as the JSON serialization/deserialization</li>
    <li>Format of the CSV:</li>
    <ul>
      <li>Rectangle: <code>&lt;id&gt;,&lt;width&gt;,&lt;height&gt;,&lt;x&gt;,&lt;y&gt;</code></li>
      <li>Square: <code>&lt;id&gt;,&lt;size&gt;,&lt;x&gt;,&lt;y&gt;</code></li>
    </ul>
  </ul>
</details>

<details>
  <summary>
    <code>models/base.py</code> - Update the class Base by adding the static method <code>def draw(list_rectangles, list_squares)</code> that opens a window and draws all the Rectangles and Squares using the Turtle graphics module. You must use the following steps to achieve this:
  </summary>
  <p>To complete this task, follow these steps:</p>
  <ol>
    <li>Ensure that you have the Turtle graphics module installed. You can install it with the following command: <code>sudo apt-get install python3-tk</code>.</li>
    <li>Create a function <code>draw_shapes</code> that uses the Turtle module to draw the shapes. You can be creative with colors, shapes, etc. (No constraints for color, shape etc… be creative!)</li>
    <li>Iterate through the list of rectangles (<code>list_rectangles</code>) and draw each rectangle using the <code>draw_shapes</code> function.</li>
    <li>Iterate through the list of squares (<code>list_squares</code>) and draw each square using the <code>draw_shapes</code> function.</li>
    <li>Display the drawn shapes in a window.</li>
    <li>Your method <code>draw</code> should be a static method.</li>
  </ol>
</details>

