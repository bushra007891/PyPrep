# Understanding Input Statements in Python
'''The input() function allows us to take input from the user while the program is running.'''
name = input("Enter your name: ")
print("Hello, " + name)

# Characteristics of input():
# Always Returns a String: 
'''Whatever the user types in, the input() function treats it as a string, even if the user enters numbers.'''
age = input("Enter your age: ")
print(type(age))  # Output: <class 'str'>

# Can Take a Prompt: 
'''The input() function can display a message (prompt) to guide the user on what to enter.'''
color = input("Enter your favorite color: ")

# Needs Typecasting for Numeric Input: 
'''If you want to use the input as a number (like in calculations), you need to convert it using typecasting (like int() or float()).'''
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Interactive: 
'''The input() function makes your programs interactive, allowing users to provide information.'''

# Customizable: 
'''You can display a message to tell the user what to enter.'''

# Flexible: 
'''Though it always takes input as a string, you can convert it to other types using typecasting.'''

# Simple to Use: 
'''With just one line, you can receive user input.'''

# Convert input to integers
num1 = int(num1)
num2 = int(num2)

sum = num1 + num2
print("The sum is:", sum)

# Types of Input
# String Input: 
'''The input() function naturally accepts string input.'''
name = input("Enter your name: ")

# Integer Input: 
'''If you need a number, you must convert the input to an integer using int().'''
age = int(input("Enter your age: "))

# Float Input: 
'''If you want a decimal number, you need to convert the input to a float using float().'''
height = float(input("Enter your height in meters: "))

