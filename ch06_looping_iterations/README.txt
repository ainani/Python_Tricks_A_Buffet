6.1 Writing Pythonic Loops
 - Iterators in Python can return more than just one value. They can return tuples with an arbitrary number of values that can then be unpacked right inside the for-statement 
 - Python’s for-loops are really “for-each” loops that can iterate directly over items from a container or sequence.

6.2 Comprehending Comprehensions
 - Python list comprehension are one liners
 - General Syntax (without condition): 
       values = [expression for item in collection]
 - General Syntax (with condition):
       values = [expression
		  for item in collection
		  if condition]
 - Comprehensions are also valid in sets and Dictionaries

6.3 List Slicing Tricks and the Sushi Operator
 - Slicing is commonly used to access ranges of elements within an ordered collection.
 - For example, you can slice up a large list object into several smaller sublists with it
 - Syntax: lst[start:end:step]
 - Operator “:” is known as sushi operator.
 - The : “sushi operator” is not only useful for selecting sublists of elements within a list. It can also be used to clear, reverse, and copy lists.
 - Creating a shallow copy means that only the structure of the elements is copied, not the elements themselves. Both copies of the list share the same instances of the individual elements.
 - If you need to duplicate everything, including the elements, then you’ll need to create a deep copy of the list. Python’s built-in copy module will come in handy for this.

6.4 Beautiful Iterators
 - Iterators are powerful because they will iterate one value at a time so memory efficient
 - While in lists we can't retrieve in infinite way
 - Python 2 and Python 3 have different next() methods
    - Python 2 have next()
    - Python 3 have __next__()
 - Iterators provide a sequence interface to Python objects that’s memory efficient and considered Pythonic. Behold the beauty of the for-in loop!
 - To support iteration an object needs to implement the iterator protocol by providing the __iter__ and __next__ dunder methods.
 - Class-based iterators are only one way to write iterable objects in Python. Other ways are generators and generator expressions.


6.5 Generators Are Simplified Iterators
 - when a return statement is invoked inside a function, it permanently passes control back to the caller of the function.
 - When a yield is invoked, it also passes control back to the caller of the function—but it only does so temporarily.
 - Whereas a return statement disposes of a function’s local state, a yield statement suspends the function and retains its local state.
 - Local variables and the execution state of the generator function are only stashed away temporarily and not thrown out completely. Execution can be resumed at any time by calling next() on the generator.
 - Generators stop generating values as soon as control flow returns from the generator function by any means other than a yield statement. This means you no longer have to worry about raising StopIteration at all!


6.6 Generator Expressions
 - Generator expressions give you an even more effective shortcut for writing iterators. 
 - With a simple and concise syntax that looks like a list comprehension, you’ll be able to define iterators in a single line of code.
 - Once a generator expression has been consumed, it can’t be restarted or reused.
 - list comprehension generates list objects while generator comprehenison generate ierable generator objects
 - Template : genexpr = (expression for item in collection if condition)
 -  Generator expressions are best for implementing simple “ad hoc” iterators. For complex iterators, it’s better to write a generator function or a class-based iterator.


6.7 Iterator Chains
 - While a regular function produces a single return value, generators produce a sequence of results. You could say they generate a stream of values over the course of their lifetime.
 - A generator output stream from one generator expression, can be given as input to another generator expression to form a pipeline
 - Data flows in one direction only, and each processing step is shielded from the others via a well-defined interface.
 - We chain together a sequence of processes so that the output of each process feeds directly as input to the next one.
 - Chained generators process each element going through the chain individually (means one by one).