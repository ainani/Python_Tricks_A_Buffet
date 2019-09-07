8.1 Exploring Python Modules and Objects
 - The Python interpreter provides a way to look into definitions of any Python module and access it's classes/methods/functions
 - This is very useful in debugging when, internet is not available and you are looking for a help for particular module/class/function
 - dir() function will be used to directly access such informations of a Python module
 - Calling dir() on a module gives you an alphabetized list of the names and attributes the module provides
 - dir() method can be used to further go deep in module to access it's classes/functions also
 - help() method can be used to get auto generated docuemntation of a Python object


8.2 Isolating Project Dependencies With Virtualenv
 - Python package manager pip can be used to install any third party packages
 - It install packages into your global Python environment by default. 
 - Which in turns make the package available globally for enviroment.
   But it also a problem if you’re working with multiple projects that require different versions of the same package.
 - Installing the packages globally may also have security issues, because pip install packages using internet which may not be trustworthy
 - Solution to such problems are virtual env of Python
 - A virtual environment is an isolated Python environment. Physically, it lives inside a folder containing all the packages and other dependencies, like native-code libraries and the interpreter runtime, that a Python project needs. 
 - Behind the scenes, those files might not be real copies but symbolic links to save memory.
 - Virtualenve is generally created in Projects directory, os that it's called as virtualenv of that project
 
 How to create a Pytohn venv ?
 - apt-get install python3-venv      : As a prerequisites to be installed 
 - python3 -m venv ./venv            : This will create a dir name venv in current working dir (venv will only work in Python3, for python 2 it's different) and seed it with python3 baseline
 - source ./venv/bin/activate        : Activate venv
 - which pip                         : will give venv pip path
 - which python                      : will give venv python path
 - pip list                          : should be blank as there are no pip packages in venv
 - pip install <package>             : install pip package in venv
 - pip list                          : List updated pip packages in venv
 - deactivate                        : Will deactivate the python venv and back to global python env

 - In venv admin passoword is not required to install packages using pip
 - all packages will be installed/updated in venv directory only
 - Virtual environments keep your project dependencies separated. They help you avoid version conflicts between packages and different versions of the Python runtime.
 - As a best practice, all of your Python projects should use virtual environments to store their dependencies. This will help avoid headaches.

8.3 Peeking Behind the Bytecode Curtain
 - Python first translates programs into byte code instructions
 - Bytecode is an intermediate language for the Python virtual machine that’s used as a performance optimization.
 - This saves time and memory for repeated executions of programs or parts of programs. 
   For example, the bytecode resulting from this compilation step is cached on disk in .pyc and .pyo files so that executing the same Python file is faster the second time around.
 - constants and code are kept seprate to save memory
 - Python stores constants separately in a lookup table. The instruction stream can then refer to a constant with an index into the lookup table
 - same is true with varnames
 - disassembler module (dis) can be used to read bytecode in more specific and readable format
 - dis will split-up the instruction stream and give each opcode in it in human readable form
 - dis put constants and varnames in stack
