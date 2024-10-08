# Understanding the print() Statement in Python
'''The print() statement is one of the most basic and important functions in Python. It allows you to display output on the screen.'''

# How Does the print() Statement Work?
'''The print() function in Python works by printing whatever you put inside the parentheses ( ). You can print:

Text (also called a string)
Numbers
Variables (things that store values)
The result of calculations'''

print("Hello, Python!")

# Characteristics of the print() Function
# Flexible
'''You can use print() to display different types of data, like strings, numbers, or even the results of mathematical operations.'''

# Easy to Use
'''You just need to write print() and put whatever you want to display inside the parentheses.'''

# Concatenation
'''You can combine (concatenate) strings and variables in the print() statement. Python automatically adds spaces between items when you separate them with commas.'''

# Escape Sequences
'''You can use special characters inside print(), like \n for a new line or \t for a tab. These are called escape sequences.'''
print("Hello\nWorld!")

# End Parameter
'''By default, print() adds a new line at the end of the output. You can change this behavior by using the end parameter.'''
print("Hello", end=" ")
print("World!")

# Types of print() Statements
'''Printing Text (Strings) You can print any text by putting it inside quotation marks (" or '). This text is called a string.'''
print("Learning Python is fun!")
print('Learning Python is fun!')

'''Printing Numbers You can also print numbers directly without quotation marks.'''
print(10)

'''Printing Variables A variable stores a value, and you can print the value by calling the variable.'''
age = 10
print(age)

'''Printing Multiple Items You can print multiple items (like text and numbers) together by separating them with commas.'''
name = "Alice"
age = 10
print("My name is", name, "and I am", age, "years old.")

'''Printing the Result of a Calculation You can use print() to show the result of a calculation directly.'''
print(5 + 3)

