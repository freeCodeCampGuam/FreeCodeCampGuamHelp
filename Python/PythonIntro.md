##Python Intro

####Types:
Here is an [intro to python](https://docs.python.org/3.5/tutorial/introduction.html) from their official docs.

TLDR:
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

```
[Explanation of slicing](http://stackoverflow.com/questions/509211/explain-pythons-slice-notation)

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

```
There are also `set()`s and tuples: `()` but we use those less often.

####How to learn as you go:

Everything in Python is an object. To see the contents of an object we can use `dir()`.

```py
dir(3.14)
# --> ['__abs__', '__add__', '__bool__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getformat__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', '__setformat__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']
```

You can also use `help(object)` within the bot's repl to display the docstrings of that object.
```py
help("some string".join)
# -->
# Help on built-in function join:
#
# join(...) method of builtins.str instance
#     S.join(iterable) -> str
#
#     Return a string which is the concatenation of the strings in the
#     iterable.  The separator between elements is S.
```

As you saw above, access an object's attributes using `.` notation.

use `dir()` and `help()` religiously to learn more about python and the libraries you use. If you need more info on them, as always, **Google** and read the docs.

