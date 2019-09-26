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
 - Operatot “:” is known as sushi operator.
 - The : “sushi operator” is not only useful for selecting sublists of elements within a list. It can also be used to clear, reverse, and copy lists.
 - Creating a shallow copy means that only the structure of the elements is copied, not the elements themselves. Both copies of the list share the same instances of the individual elements.
 - If you need to duplicate everything, including the elements, then you’ll need to create a deep copy of the list. Python’s built-in copy module will come in handy for this.

 - 
