4.1 Object Comparisons: “is” vs “==”
 - The == operator compares by checking for equality
 - The is operator, however, compares identities
 - An is expression evaluates to True if two variables point to the same (identical) object.
 - An == expression evaluates to True if the objects referred to by the variables are equal (have the same contents).  



4.2 String Conversion (Every Class Needs a __repr__)
 - method starting and ending with __ (double underscores) in Python are known as dunder (double underscore) methods
 - __init__ is called as object constructor in Python
 - __str__ is one of Python’s “dunder” (double-underscore) methods and gets called when you try to convert an object into a string through the various means that are available
