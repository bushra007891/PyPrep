# Understanding type() Function and Typecasting in Python
# The type() Function
'''The type() function is used to find out the data type of a variable or value. It helps you understand whether a value is an integer, a string, a list, or something else.'''
a = 10
b = "Hello"
c = [1, 2, 3]

print(type(a))  # Output: <class 'int'>
print(type(b))  # Output: <class 'str'>
print(type(c))  # Output: <class 'list'>

# Characteristics of type() and Typecasting
# Helps Identify Data Types: 
'''The type() function allows you to check the type of any variable or value in your program.'''

# Simplifies Code: 
'''By knowing the data type, you can avoid errors, especially when performing operations.'''

# Implicit Typecasting is Safe: 
'''Python handles implicit conversions automatically, so there’s no risk of data loss.'''

# Explicit Typecasting Offers Control: 
'''You can manually convert data types when necessary, which is useful when working with mixed data types.'''

# Versatile Typecasting Functions: 
'''Python offers various functions (int(), float(), str(), etc.) for converting values to different types.'''

# Typecasting (Type Conversion)
'''Typecasting is the process of converting one data type into another.'''

# There are two types of typecasting:
'''Implicit Typecasting (done automatically by Python): In implicit typecasting, Python automatically converts one data type to another without the need for you to manually change it. This happens when there is no risk of data loss.'''
x = 5    # Integer
y = 2.5  # Float

result = x + y
print(result)         # Output: 7.5 (float)
print(type(result))   # Output: <class 'float'>

'''Explicit Typecasting (done manually by the programmer): In explicit typecasting, you manually convert a value from one data type to another using built-in Python functions such as:
int() – to convert to an integer
float() – to convert to a float
str() – to convert to a string
list() – to convert to a list, etc.'''
a = "100"
b = 20

# Convert string to integer for addition
a = int(a)

result = a + b
print(result)  # Output: 120

# Types of Typecasting
# int(): 
'''Converts a value into an integer (removes the decimal part if it’s a float).
Example: int(5.6) becomes 5'''

# float(): 
'''Converts a value into a floating-point number (adds decimal point if needed).
Example: float(5) becomes 5.0'''


# str(): 
'''Converts a value into a string.
Example: str(10) becomes "10"'''

# list(): 
'''Converts a value, such as a tuple or a set, into a list.
Example: list((1, 2, 3)) becomes [1, 2, 3]'''

# tuple(): 
'''Converts a list or set into a tuple.
Example: tuple([1, 2, 3]) becomes (1, 2, 3)'''

# bool():
'''Converts a value into a boolean (True or False).
Example: bool(0) becomes False, bool(1) becomes True'''

