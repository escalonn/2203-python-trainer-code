## Python Review
- High Level Programming language
    - Automatic memory management
    - Garbage Collection
    - no pointers for developers
- Dynamically Typed Language
    - You do not need to declare types
    - There are optional type annotations
        - are only for hinting and have 0 effect on actual code execution
- Strongly Typed Language
    - Variables cannot be implicitly coerced into other types
        - "Hello" + 100
- Interpreted Language
    - Python executes line by line
        - JIT Just in Time Compilations where each statement is turned into machine code then executed as the program runs
    - There is no compiling phase
    - Different from language like C or C++ or Java
    - Being an interpreted language means that so long as you follow the languages specification and syntax you could run it on anything.

### Operators and key words

```python
+ addition
- subtract
/ divide
* multiply
** power
% modulo
// floor division
< less than
<= less than or equal
> greater than
>= greater than or equal
== equal
!= not equal

def # defines the start of a function
class # start of a class definition
assert # raises an assertion error if not true
del # deletes variables and collection members

# control flow
if
elif
else
for, in
while
break
continue
return
yield

# boolean
not
and
or
is, is not
in, not in
True
False

# python uses None instead of null
None

# importing
from, import, as

# Exceptions
try
except
finally
with
raise

# other
pass
lambda
```

### Scopes in Python
Python follows LEGB scoping/namespaces

- Local
- Enclosing
- Global
- Built-in
    - (but you should NEVER name a variable that uses the same name has a built-in variable. i.e id )


### Strings
- Strings are immutable.
    - once created they cannot be altered
- Strings are created by doing x = "some string"
- String slicing "Hello"[2:5:-1]

### Classes and Objects

- In Python EVERYTHING is an object
    - Strings, ints, floats, booleans
    - There are not primitive data types like in Java
- You can create your own objects using classes
    - classes are blueprints to create objects
- objects can have instance variables and methods
    - methods are functions attached to a class

```python

class Person:
    total_people = 0 # define the Class variables at the top
    # Static variables if you are used to Java

    #__init__ is the constructor in Python
    # Python DOES NOT support overloading
    # instance variables are created by doing self.x = some_value
    def __init__(self, name, age):
        #self is like 'this' in Java/C#/JS classes
        self.name = name
        self.age = age
        Person.total_people = Person.total_people +1

    # Methods take self as the first parameter
    def say_hello(self):
        print(f"Hello my name is {self.name}")

    # DUNDER double_underscore methods
    # special methods in python used for common operations

    # whenever you use str(object) it calls this method
    # print() calls this, str.format and f-strings call this
    # human-friendly string version
    def __str__(self) -> str:
        return f"name: {self.name}"

    # what to do when this object is used with a + operator (object + 10)
    def __add__(self, object):
        pass

    #representation
    # a string representation of the object that has all the fields and can be used to recreate the object if need be
    # machine-parsing-friendly string version
    def __repr__(self):
        return ""

```
### Collections
All collections can store ANY type of object

- Lists
    - Mutable (append and remove elements)
    - Can contain duplicates
    - Lists are indexable my_list[34]
- Sets
    - Mutable (append and remove elements)
    - CANNOT contain duplicates
- Tuples
    - Immutable (Cannot add or remove elements or edit the values)
    - Tuples are indexable my_tuple[34]
- Dicitonaries
    - Mutable (append and remove elements)
    - Key value pairs
    - Cannot have duplicate keys

```python
l = [1,2,2,4] # List
s = {1,2,3,4} # Set
t = (1,2,3,4,5,5,5,6) # Tuple
d = {"a":1, "b":2, "c":3} # Dictionary
```
|Collection|Mutable|Duplicates|Indexable/Ordered|
|----------|-------|----------|-----------------|
|list      |Yes    |Yes       |Yes              |
|Set       |Yes    |No        |No               |
|Tuples    |No     |Yes       |Yes              |
|Dictionary|Yes    |No (keys) |Yes (since 3.7)  |

### Exceptions
- Occur when code does NOT execute "according to plan"
    - raising an exception
- exceptions are just objects that contain information about what went wrong
- In built exceptions you should be aware of
    - Exception
        - The parent class of all Errors in Python
    - NameError
        - occurs when you reference a variable that does not exist
    - LookupError
        - parent class of KeyError and OutOfBoundsError
    - TypeError
        - Something of the wrong type is being used
    - ValueError
        - Right type but the value is inappropriate
- can create custom errors
```python
class MyCustomError(Exception):
    #code
```
Basic syntax for handling errors
```python
try:
    #code that might fail and raise an exception
    if something:
        raise ValueError("That is a wrong value")
except ValueError as e:
    # code to handle error
    str(e) # to get error message
except Exception as e:
    # a catch all except block (should go last)
finally:
    #code that will always execute even if nothing goes wrong
```
### Importing and file/code Management
- Every python file is called a **Module**
- A folder containing python modules is called a **package**

```python
from package import module
module.foo()

from package.module import foo
foo()
```

### pip, PyPi, venv
- pip
    - pip is the main package installation software that comes with python
    - the main to download python packages/code from the web
    - It will install it globally on your machine if not in a virtual environment
    - Similar to npm for node or maven for Java
- PyPi
    - The main Python repository
    - Contains millions of python packages for anything software related
    - Similar to Maven Central repo for Java or npm repository for node
- venv
    - If you write a python application using modules installed via PyPi it can be hard to track which
    packages/modules are actually used by your application vs just installed from a previous project
    - venv (virtual environment) creates a venv folder that stores python packages for a single project
    - Allows you to manage versions of packages you are using as well as only including ones you need
    - This becomes VERY helpful when you need to get your Python program to run on another machine
