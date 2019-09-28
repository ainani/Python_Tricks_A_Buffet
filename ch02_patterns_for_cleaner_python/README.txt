2.1. Covering Your A** With Assertions

 - Proper use of assertions is to inform developers about unrecoverable errors in a program.
 - Assertions are not intended to signal expected error conditions, like a File-Not-Found error, where a user can take corrective actions or just try again.
 - Assertions are meant to be internal self-checks for your program.
 - They work by declaring some conditions as impossible in your code. If one of these conditions doesn’t hold, that means there’s a bug in the program.
 - If your program is bug-free, these conditions will never occur. But if they do occur, the program will crash with an assertion error telling you exactly which “impossible” condition was triggered.
 - This makes it much easier to track down and fix bugs in your programs. And I like anything that makes life easier—don’t you?
 - For now, keep in mind that Python’s assert statement is a debugging aid, not a mechanism for handling run-time errors.
 - The goal of using assertions is to let developers find the likely root cause of a bug more quickly.
 - An assertion error should never be raised unless there’s a bug in your program.



Assertion checking can be stopped by using -O option in command line
 - Means assertion will be compiled but not evaluated


1. Assertion should not be used for data validation
  - Because if assertion is disabled during execution it will be a security threat in few cases. like : checking for admin user or checking if a product really exist in list before deleting it
2. Assert syntax, 
   assert(1==2, 'This will never fail') 

   This assert will never fails as it will not evaluate to False any time.
   In Python any non-empty tuple is considered as True only. So above assert will never fails



 - Python’s assert statement is a debugging aid that tests a condition as an internal self-check in your program.
 - Asserts should only be used to help developers identify bugs. They’re not a mechanism for handling run-time errors.
 - Asserts can be globally disabled with an interpreter setting



2.2 Complacent Comma Placement
 - Most source control systems are line-based and have a hard time highlighting multiple changes to a single line.
   So for best practice multi-line declaration of list and dict variables
   list1= [
	   a,
	   b,
	   c
          ]

2.4 Underscores, Dunders, and More
 1. Single Leading Underscore: “_var” 
    Means, variable is used for internal usage

    PEP 8 recommendation that wildcard imports should be avoided, then all you really need to remember is this

    Single underscores are a Python naming convention that indicates a name is meant for internal use. It is generally not enforced by the Python interpreter and is only meant as a hint to the programmer.

 2. Single Trailing Underscore: “var_”
   In summary, a single trailing underscore (postfix) is used by convention to avoid naming conflicts with Python keywords.


 3. Double Leading Underscore: “__var”


 4. Double Leading and Trailing Underscore: “__var__” 
    However, names that have both leading and trailing double underscores are reserved for special use in the language. 
    This rule covers things like __init__ for object constructors, or __call__ to make objects callable.   

 5. Single Underscore: “_”
    - Used as a name to indicate that a variable is temporary or insignificant.    
    - Used in unpacking expressions as a 'don't care' variable to ignore particular values
    - '_' can be used as result of last expression evaluated by Python interpreter
    - can be also used when defining objects on the fly without giving name to them initally


  • Single Leading Underscore “_var”: Naming convention indicating a name is meant for internal use. Generally not enforced by the Python interpreter (except in wildcard imports) and meant as a hint to the programmer only.
  • Single Trailing Underscore “var_”: Used by convention to avoid naming conflicts with Python keywords. 
  • Double Leading Underscore “__var”: Triggers name mangling when used in a class context. Enforced by the Python interpreter.
  • Double Leading and Trailing Underscore “__var__”: Indicates special methods defined by the Python language. Avoid this naming scheme for your own attributes.
  • Single Underscore “_”: Sometimes used as a name for temporary or insignificant variables (“don’t care”). Also, it represents the result of the last expression in a Python REPL session.


2.5 A Shocking Truth About String Formatting
  #1 – “Old Style” String Formatting
     - Using % sign 
  #2 – “New Style” String Formatting
     - Calling format() in string object
  #3 – Literal String Interpolation (Python 3.6+)
     - f'{}
  #4 – Template Strings
     - Template() 
