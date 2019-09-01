Python’s functions are first-class objects. 
 - Can be assigned to variables
 - Can be stored in data structures, pass them as arguments to other functions, and 
 - even return them as values from other functions.

- As everything in Python is an object, Python's functions are also an object
- so a declared function can be assinged to another variable 

- Functions that can accept other functions as arguments are also called higher-order functions.
   like map()  --> map(function, iterable)   --> Return an iterable (list, dict or tuple)


3.2 Lambdas Are Single-Expression Functions
 - The lambda keyword in Python provides a shortcut for declaring small anonymous functions.
 - Lambda functions behave just like regular functions declared with the def keyword.
 - They can be used whenever function objects are required.
 - Lambda expressions can be used to just write functions inline without using def keyword and function name
 - Since lambda functions doesn't need a name they are also known as anonymous functions
 - Lambda expressions have implict return statement that it will return the evaluated expression after executing it.
 - Since lambda doesn't return explicitly they are known as single expression functions
 - Whenever you’re expected to supply a function object you can use a lambda expression
 - Lambda functions should be used sparingly and with extraordinary care.
 - map() and filter() should also be used with care, instead use list comprehension or generators
 - Lambda functions are single-expression functions that are not necessarily bound to a name (anonymous).
 - Lambda functions can’t use regular Python statements and always include an implicit return statement.
 - Always ask yourself: Would using a regular (named) function or a list comprehension offer more clarity?

3.5 Function Argument Unpacking
 - * can be used to unpack the lists, tuples and generators in Python.
 - It can be used to pass whole lists, tuples or generators to a Python functions as an argument
 - Putting a * before an iterable in a function call will unpack it and pass its elements as separate positional arguments to the called function
 - ** can be used to unpack dictionaries
 - Because dictionaries are unordered, this matches up dictionary values and function arguments based on the dictionary keys: 
   the x argument receives the value associated with the 'x' key in the dictionary.
 - If you were to use the single asterisk (*) operator to unpack the dictionary, keys would be passed to the function in random order instead
 - Unpacking is very useful in Python, you won’t have to implement a class for a data type needed by your program. 
   As a result, using simple built-in data structures like tuples or lists will suffice and help reduce the complexity of your code.

3.6 Nothing to Return Here
 - By default Python functions return "None", if no return statemnet is mentioned at end of a function
 - If a function doesn’t specify a return value, it returns None.
