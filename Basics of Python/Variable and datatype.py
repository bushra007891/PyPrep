# Understanding Variables and Data Types in Python
# Variable
'''A variable in Python is like a container that stores data.'''

# Characteristics of Variables:
# Stores Data: 
'''Variables hold data that you can use throughout your program.'''

# Dynamic Typing: 
'''In Python, you don’t need to specify the type of data when creating a variable. Python automatically knows the type based on the value.'''

# Easy to Change:
'''You can easily update the value of a variable at any time.'''

name = "Alice"  # A variable 'name' storing a string value
age = 10  # A variable 'age' storing a number (integer) value

# Data Type
'''Data types define what kind of data a variable can hold.'''

# Characteristics of Data Types:
# Defines the Type of Data:
'''Each variable has a specific data type that determines what kind of data it can hold.'''

# Operations Depend on Type:
'''Different operations are allowed for different data types (you can't add a number to a string, for example).'''

# Memory Efficiency:
'''Python uses different amounts of memory to store different types of data.'''

# Type Conversion:
'''Python allows you to convert from one data type to another, like changing an integer to a string using str()'''
age = 10  # Integer
age_string = str(age)  # Convert integer to string
print(age_string)  # Outputs: '10'

# Types of Data Types in Python:
# Numeric Types
'''These are used to store numbers.
Integer (int): Stores whole numbers, like 5, -3, or 100.
Float (float): Stores decimal numbers, like 5.2, -3.7, or 100.0.'''
x = 10  # Integer
y = 3.14  # Float

# Text Type
'''This is used to store sequences of characters, like words or sentences.
String (str): A string is used for text and is surrounded by quotes.'''
greeting = "Hello, World!"  # String

# Boolean Type
'''This type is used to represent True or False values.
Boolean (bool): Stores either True or False.'''
is_student = True  # Boolean

# Sequence Types
'''These store collections of items, like lists of numbers or words.
List (list): A list is a collection of items that can be of different types, and it is surrounded by square brackets [ ].'''
numbers = [1, 2, 3, 4, 5]  # List of integers

# Mapping Type
'''A mapping type stores key-value pairs.
Dictionary (dict): A dictionary stores data as key-value pairs, surrounded by curly braces { }.'''
person = {"name": "Alice", "age": 10}  # Dictionary with name and age

