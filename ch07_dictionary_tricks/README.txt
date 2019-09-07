7.1 Dictionary Default Values
 - Python's dictionary get() method support 'default' fallback value in case any KeyError exception is raised.
 - dict1.get(key, <default value>)
 - If key is not present in dictionary, it will return the provided  default value (if get method is used)


7.2 Sorting Dictionaries for Fun and Profit
 - Python's dictionary can't gurantee to be iterated in order.
 - Sorting on keys is gerally used to iterate dictionary in ordered manner
 - sorted(dict1.items()) --> Will sort te dict items based on keys and stored them as list of tuples
 - Two tuples are compared by comparing the items stored at index zero first. If they differ, this defines the outcome of the comparison. 
   If they’re equal, the next two items at index one are compared, and so on.
 - Since, keys of a dict are unique so resulted list of tuples (after sorting dict) will also have unique values of tuple at index ZERO.
   This will not help in comparing tuples
 - To overcome this, Python have another function key(), which can control the order during sorting.
 - A key func is simply a normal Python function to be called on each element prior to making comparisons. 
   The key func gets a dictionary item as its input and returns the desired “key” for the sort order comparisons.
 - operator.itemgetter() can be also used instead of lambda in key function
 - Generally, lambda function is preferred over operator.itemgetter() if user need to sort iterable based on customised keys. Else operator.itemgetter() is best suited

7.3 Emulating Switch/Case Statements With Dicts
 - Python doesn't have Switch/Case statement
 - Alternative is to use long if-elif....else loops
 -  Another alternative is using dictionaries and functions (as first-class objects)

7.4 The Craziest Dict Expression in the West
 - When Python processes our dictionary expression, it first constructs a new empty dictionary object; and then it assigns the keys and values to it in the order given in the dict expression. 
 - Python consider bool as subclass of integer
 - And yes, this means you can technically use bools as indexes into a list  or tuple in Python:
 - Python dict done's modify the key objects if a new value is assigned to the key
 - Python dictionaries are backed by a hash table data structure
 - a hash table internally stores the keys it contains in different “buckets” according to each key’s hash value
 - The hash value is derived from the key as a numeric value of a fixed length that uniquely identifies the key.
 - This allows for fast lookups. It’s much quicker to search for a key’s  numeric hash value in a lookup table instead of comparing the full key object against all other keys and checking for equality.
 - hash collision : A situation where 2 or more keys having same hash value

7.5 So Many Ways to Merge Dictionaries
 - Using used defined method to merge dicts
 - Using dictionaries builtin method update()
 - Using **dict to merge the dictionaries
 - In **dict, order will be from left-to-right and right dict will have preference over left

7.6 Dictionary Pretty-Printing
 - using json.dumps(), we can print the dictionary is more readable format
 - json.dumps() works only for primitive data-types, cannot use json.dumps() on non-primitive datatypes
  >>> json.dumps({all: 'yup'})
      TypeError: "keys must be a string"  
 - complex dataypes like sets cannot be printed using json.dumps()
   >>> mapping['d'] = {1, 2, 3}
   >>> json.dumps(mapping)
       TypeError: "set([1, 2, 3]) is not JSON serializable"
 - pprint is other alternative and best suits over json.dumps() as it's cover all possible limitaitons of json.dumps()

