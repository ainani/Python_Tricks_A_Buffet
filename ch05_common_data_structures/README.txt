5.1 Dictionaries, Maps, and Hashtables
 - Centralized data structure in Python stores arbitrary number of objects mapped using key
 - Often called maps, hashmaps, lookup tables, or associative arrays 
 - fast lookup, insertion and deletion of objects using key 
 - A hashable object has a hash value which never changes during its lifetime (see __hash__), and it can be compared to other objects (see __eq__).
 - Immutable types like strings and numbers are hashable and work well as dictionary keys. 
 - Tuples can also be used as dict keys if they are hashable
 - Complexitiy of dict : O(1) time complexity for lookup, insert, update, and delete operations in the average case. 
 - collections.OrderedDict – Remember the Insertion Order of Keys
 - collections.defaultdict – Return Default Values for Missing Keys
 - collections.ChainMap – Search Multiple Dictionaries as a Single Mapping
   - groups multiple dictionaries into a single mapping
   - Lookups search the underlying mappings one by one until a key is found
   - return keyError exception in case key is not found
 - types.MappingProxyType – A Wrapper for Making Read-Only Dictionaries


5.2 Array Data Structures
 - Arrays consist of fixed-size data records that allow each element to be efficiently located based on its index.
 - Because arrays store information in adjoining blocks of memory, they’re considered contiguous data structures (as opposed to linked datas structure like linked lists, for example.)
 - Performance-wise, it’s very fast to look up an element contained in an array given the element’s index. A proper array implementation guarantees a constant O(1) access time for this case. 

 list – Mutable Dynamic Arrays
 - list automatically allocate and release memory 
 - since everythin in Python is object, so list can contains multiple data types stored in it
 - this is powerful feature, but the problem is whole data structured is less tightly packed due to multiple data types. This will takes up more space

 tuple – Immutable Containers
 - all elements in a tuple must be defined at creation time because tuples are immutable
 - tuples have same property as lists

 array.array – Basic Typed Array
 - Possess similar property as C
 - Very much similar to Python lists, but can have only single data type
 - Due to single data type restriction array.array objects with many elements are more space-efficient than lists and tuples. 
 - The elements stored in them are tightly packed, and this can be useful if you need to store many elements of the same type.

 str – Immutable Arrays of Unicode Characters 
 - each character in a string is a str object of length 1 itself
 - String objects are space-efficient because they’re tightly packed and they specialize in a single data type.
 - If you’re storing Unicode text, you should use them. Because strings are immutable in Python, modifying a string requires creating a modified copy. 
 - The closest equivalent to a “mutable string” is storing individual characters inside a list
 - Strings are recursive data structures, means a string is collections of single character string

 bytes – Immutable Arrays of Single Bytes
 - Bytes objects are immutable sequences of single bytes (integers in the range of 0 <= x <= 255)
 - Conceptually they are similar to str objects
