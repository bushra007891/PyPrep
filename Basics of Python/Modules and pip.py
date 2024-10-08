# Understanding Python Modules and pip
# Modules
''' A module is like a toolbox filled with ready-made tools (functions, classes, etc.) that you can use in your programs.'''

# Characteristics of Modules:
# Reusable Code
'''Modules allow you to reuse code in different programs, saving time and effort.'''

# Organized Code
'''Instead of writing everything in one big file, you can organize your code into modules, making it easier to manage.'''

# Pre-built Functions
'''Modules contain pre-written functions that you can use instantly. This makes your program more powerful with less work.'''

# Built-in and External
'''You have access to both built-in modules and external modules, giving you a wide range of tools.'''

# Easy Importing
'''You can import a module with just one line of code and start using its functions right away.'''

# There are two types of modules in Python:
# Built-in Modules
'''These are modules that come with Python, so you don’t need to install them. You just import them and start using them. Some popular built-in modules include:'''

# math: Provides mathematical functions like sqrt() (square root) or pow() (power).
import math
print(math.sqrt(16))

# random: Helps you generate random numbers.
import random
print(random.randint(1, 10))

# datetime: Lets you work with dates and times.
import datetime 
print(datetime.datetime.now())

# External Modules (Third-Party Modules)
'''These are modules created by other Python developers and shared with the community. You can download and install these modules using pip. For example:'''

# requests: Helps you work with web data, like making HTTP requests.
# numpy: Useful for mathematical operations with large datasets.'''

# pip
'''On the other hand, pip is a tool that helps you download and install these modules from the internet so you can use them in your Python projects.'''

# Characteristics of pip:
# Easy Installation
'''pip makes it simple to download and install external modules by typing a single command.'''

# Wide Availability
'''pip has access to thousands of external modules, making it easy to find and use the tools you need.'''

# Dependency Management
'''When you install a module using pip, it also installs any other modules that the module depends on (called dependencies).'''

# Version Control
'''You can use pip to install specific versions of a module or update an existing module.'''

# Uninstalling
'''Just as you can install a module with pip, you can also remove it by typing:'''

