##Python Intro

*edit:
After I wrote this page, I found a more in-depth, better written article online!  
[Learn Python in 10 minutes](https://www.stavros.io/tutorials/python/).   It's an introduction to python 2. We're using python 3, so there will be some differences.  

| Python 2 | Python 3 |
| -------- | -------- |
| `print "stuff"` | `print("stuff")` |
| `xrange(n)` | `range(n)` |
| N/A | `async` and `await` |
| `3 / 2 == 1` | `3 / 2 == 1.5` |  

Here is the official introduction from the Python docs as well: [intro to python](https://docs.python.org/3.5/tutorial/introduction.html)

TLDR:  

###How to learn as you go:

Test small things in your REPL, whether that be on Discord or in your text editor.  

Everything in Python is an object. To see the contents of an object we can use `dir()`.

```py
dir(3.14)
# --> ['__abs__', '__add__', '__bool__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getformat__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', '__setformat__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']
```

You can also use `help(object)` within the bot's repl to display the docstrings of that object.
```py
help("some string".startswith)
# -->
# Help on built-in function startswith:
# 
# startswith(...) method of builtins.str instance
#     S.startswith(prefix[, start[, end]]) -> bool
#     
#     Return True if S starts with the specified prefix, False otherwise.
#     With optional start, test S beginning at that position.
#     With optional end, stop comparing S at that position.
#     prefix can also be a tuple of strings to try.
```

As you saw above, you can access an object's attributes using `.` notation.

You can also see an object's docstring using `.__doc__`. `help(object)` will show all the docstrings of all the attributes of the object. `.__doc__` will show you only the object's docstring.

```py
help(True)
# --> 
# Help on bool object:
# 
# class bool(int)
#  |  bool(x) -> bool
#  |  
#  |  Returns True when the argument x is true, False otherwise.
#  |  The builtins True and False are the only two instances of the class bool.
#  |  The class bool is a subclass of the class int, and cannot be subclassed.
#  |  
#  |  Method resolution order:
#  |      bool
#  |      int
#  |      object
#  |  
#  |  Methods defined here:
#  |  
#  |  __and__(self, value, /)
#  |      Return self&value.
#  ...


True.__doc__
# -->
# bool(x) -> bool
#
# Returns True when the argument x is true, False otherwise.
# The builtins True and False are the only two instances of the class bool.
# The class bool is a subclass of the class int, and cannot be subclassed.
```

Use `dir()`, `help()`, and `__doc__` religiously to learn more about python and the libraries you use. If you need more info on something, as always, **Google**, read the docs, and ask us.  
Most likely we'll know something you don't or you'll share with us something we don't know.  
I used `ans.startswith('y') or ans.startswith('both')` before writing this tutorial.  
Now I know that I can do this instead: `ans.startswith(('y','both'))`

###Types:  
```py
# this is a comment

my_var = 5  # I just assigned the number 5 into my_var
food = "burger"  # this is a string
other_string = 'this is also a string'

other_string[0]
# --> 't'

# a list in Python is like an array or arraylist in other languages
# it can hold multiple types of data

a_list = [1, 2, -3, 'dog', True, False, None]

# notice, None is Python's null value and True/False have their first letter capitalized

a_list[0]
# --> 1

a_list[3]
# --> 'dog'

# you can use negitive indices also
a_list[-1]
# --> None

a_list[-2] = 3.14
# --> [1, 2, -3, 'dog', True, 3.14, None]

# you can easily slice python arrays and strings
a_list[3:]
# --> ['dog', True, 3.14, None]

# you can use negitive numbers when slicing as well.
a_list = a_list[3:-1]
# --> ['dog', True, 3.14]

# use .append() to add something to the end of a list
a_list.append('end')
# --> ['dog', True, 3.14, 'end']

# and use .pop() to take something out of the list.
# if no index is specified, the item is taken off the end of the list.
a_list.pop(0)
# --> "dog"
# --> [True, 3.14, 'end']
```
[Explanation of slicing](http://stackoverflow.com/questions/509211/explain-pythons-slice-notation)  

Dicts are like associative arrays or hash tables. Dicts are an unordered set of key value pairs. You cannot have 2 items with the same key in a dict.
```py
my_dict = {
	"dog" : "bone",
	"cat" : "catnip",
	"mouse" : "cheese"
}

my_dict["dog"]
# --> "bone"

my_dict["human"] = "chips"
# --> {"dog" : "bone", "cat" : "catnip", "mouse" : "cheese", "human" : "chips"}

# replacing "bone" with "bacon"
my_dict["dog"] = "bacon"
# --> {"dog" : "bacon", "cat" : "catnip", "mouse" : "cheese", "human" : "chips"}
```
There are also `set()`s and tuples: `()` but we use those less often.

###Control Flow and Conditionals:

Python doesn't use semicolons and brackets to denote control flow depth.
Instead, it uses the colon `:` to denote a new layer of depth and tabs **or** spaces to show what lines are within that depth.  
**Do not mix tabs and spaces.** You will get a error.  
By convention, Python uses 4 spaces (or 4 tab-width) per level.

```py
if False:
    print('hi')
	print('there')
print('how are you?')
# --> how are you?
```

* **Conditionals**

| syntax | explanation |
| ------ | ----------- |
| `==` | equality |
| `!=` | inequality |
| `<` | less than |
| `>` | greater than |
| `<=` | less than or equal to |
| `>=` | greater than or equal to |  

*[explanation of `is` vs. `==`](http://stackoverflow.com/questions/2988017/string-comparison-in-python-is-vs)

* **`if`/`elif`/`else`**
```py
a = 0

if a < 5:
    print('hi')
# --> hi

if a >= 5:
    print('hi')
else:
    print('bye')
# --> bye

if a > 5:
    print('hi')
elif a == 0:
    print('hello?')
else:
    print('bye')
# --> hello?

# you can also check for values within a range
if 0 < a < 100:
    print('a is between 0 and 100 exclusive')
else:
    print('a is not between 0 and 100')
# --> a is not between 0 and 100
```

* **loops**  

```py
# while

i = 0
numbers = []
while i != 5:
    numbers.append(i)
    i += 1  # note, there is no i++ in Python
print(numbers)
# --> [0, 1, 2, 3, 4]

# for

numbers = []
for i in range(0,5):
    numbers.append(i)
print(numbers)
# --> [0, 1, 2, 3, 4]

# syntax is  for variable in iterable:
for i in numbers:
    print(i * 2)
# -->
# 0
# 2
# 4
# 6
# 8

```
* **logical operators and `in`**

| syntax | explanation |
| ------ | ----------- |
| and | logical AND.  `True and True` is True. `True and False` is False |
| or | logical OR. `True or False` is True. `False or False` is False |
| not | logical NOT. `not True` is False. `not False` is True |  

```py
a = 0
b = 10

if a < 6 and b > 6:
    print('yup')
# --> yup

if a == 10 or b == 10:
    print('one is 10')
# --> one is 10

if not a == 10:
    print('it wasn\'t a')
# --> it wasn't a
```

`in` and `not in` are used to test for membership  

```py
li = [1,2,3]

if 2 in li:
    print('yup')
# --> yup

if 4 not in li:
    print('missing')
# --> missing

# you can check for containment in strings
phrase = "the quick brown fox"

if 'fox' in phrase:
    print('fox is here')
# --> fox is here

# you can check for containment in dict keys also
basket = {'apple': 2, 'pear': 1}

if 'pear' in basket:
   print('got a pear')
# --> got a pear
```

* **Functions**

Simple function:  
```py
def hello():
    print('hello world')

hello()
# --> hello world
```

Functions can take parameters:
```py
def hello(name):
    print('hello {}'.format(name))

hello('Bob')
# --> hello Bob

def hello(first, last):
    print('hello {} {}'.format(first, last))

hello('John', 'Smith')
# --> hello John Smith
```

You can specify what type a parameter should be.
```py
def even(num: int):
    return num % 2 == 0

if even(6):
    print('even')
# --> even
```

You can specify optional parameters but they must be after the required parameters
```py
def hello(name=None):
    if name is None:
   	  	print('hi there')
    else:
      	print('hello {}'.format(name))

hello()
# --> hi there

def hello(first, last, middle=None):
    if middle is None:
        print('hello {} {}'.format(first, last))
    else:
        print('hello {} {} {}'.format(first, middle, last))

hello('John', 'Bob', 'Smith')
# --> hello John Bob Smith
```

* **Classes are blueprints for objects.**  

```py  
from random import choice

class Dog:
    """this is Dog's docstring. It can be multiple lines. 
	Having one is prefered but not required.
    """

    def __init__(self, name, owner=None):
        """each class should have a constructor.
        It gets called when making a new object from a class."""
	   
	    # within __init__ we define the object's attributes
	    # self refers to the object itself
        self.name = name
        self.owner = owner
        self.wagging = True
        self.barks = ['arf','bark','bow-wow','howl','woof']

	# an object can have methods (functions).
	# notice, self is always the 1st parameter.
	def is_happy(self):
	    return self.wagging

    def bark(self, target: str=None):
    	"""random bark or barks at someone"""
    	chosen_bark = choice(self.bark)
		if target is None or target == self.owner:
		    print(chosen_bark)
		else:
			print('{} {}s at {}'.format(self.name, chosen_bark, target))
```

* **Using classes**  

using the above Dog class:
```py
rover = Dog('Rover')
gimpy = Dog('Gimpy', 'John')

if rover.is_happy():
   rover.bark()
# --> bow-wow

rover.bark('John')
# --> Rover howls at John

gimpy.bark('John')
# --> arf

rover.owner = 'John'
rover.bark('John')
# --> woof

print(rover.owner)
# --> John
```

* **docstrings are how you document your classes.** (and are what the `!help` command uses in Red-DiscordBot)

```py
help(rover)
# -->
# Help on Dog in module builtins object:# 

# class Dog(object)
#  |  this is Dog's docstring. It can be multiple lines. 
#  |  Having one is prefered but not required.
#  |  
#  |  Methods defined here:
#  |  
#  |  __init__(self, name, owner=None)
#  |      each class should have a constructor.
#  |      It gets called when making a new object from a class.
#  |  
#  |  bark(self, target:str=None)
#  |      random bark or barks at someone
#  |  
#  |  is_happy(self)
# ...

rover.__doc__
#--> 
# this is Dog's docstring. It can be multiple lines. 
#     Having one is prefered but not required.

dir(rover)
# [__dir__, __doc__, ..., 'bark', 'barks', 'is_happy', 'name', 'owner', 'wagging']
```

[Go back](README.md) and learn about `async` and Red commands




