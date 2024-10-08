# Functions and Recursion in Python
# Functions
'''A function is a set of statements that perform a specific task.'''
def greet():
    print("Hello, welcome to Python!")

greet()  # Calling the function

# Why use functions?
# Reusability: 
'''Write the code once and use it multiple times.'''

# Organization: 
'''Break your program into smaller, manageable pieces.'''

# Clarity: 
'''Makes your code easier to understand.'''

# Types of functions:
# Built-in Functions: 
'''These are functions that come with Python, like print(), len(), etc.'''

# User-defined Functions: 
'''These are functions you create yourself, like the greet() function in the example above.'''

# Arguments and Parameters:
'''Arguments are values you pass to a function when calling it.
Parameters are variables in the function that hold the values passed as arguments.'''
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)  # Arguments are 5 and 3
print(result)  # Output: 8

# Return Statement:
'''A function can return a value using the return keyword. This allows the function to give back a result after processing.'''
def square(x):
    return x * x

result = square(4)  # Function returns 16
print(result)

# Recursion
'''Recursion is a technique where a function calls itself to solve a problem.'''
def factorial(n):
    if n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call

result = factorial(5)
print(result)  # Output: 120

# How does recursion work?
'''A recursive function must have a base case to stop the recursion; otherwise, it will continue indefinitely.
It solves smaller versions of the problem in each recursive call until the base case is reached.'''

# Characteristics of recursion:
# Base Case: 
'''The condition that stops the recursion.'''

# Recursive Case: 
'''The part where the function calls itself to break down the problem.'''

# Types of Recursion:
# Direct Recursion: 
'''A function directly calls itself.'''

# Indirect Recursion: 
'''A function calls another function, which in turn calls the first function.'''

# Advantages of Recursion:
'''Helps in solving problems that can be divided into sub-problems, like factorial calculation or searching algorithms.'''

# Disadvantages of Recursion:
'''Can lead to performance issues if not properly designed.
Requires more memory due to function calls stacking up.'''


















