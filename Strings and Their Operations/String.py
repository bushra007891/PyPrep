# Understanding Strings in Python
'''A string is a sequence of characters. In simple terms, anything you write between quotes in Python is considered a string.'''
name = "Alice"
greeting = 'Hello, World!'

# Characteristics of Strings:
# Strings are Immutable: 
'''Once you create a string, you cannot change its individual characters. You can create a new string, but you can’t modify the existing one.'''
name = "Alice"
name[0] = "C"  # This will cause an error because strings cannot be changed.

# Strings Can Be Indexed: 
'''Every character in a string has a position (index) that starts from 0. You can access characters using these indexes.'''
name = "Alice"
print(name[0])  # Output: A
print(name[1])  # Output: l

# Strings Can Be Sliced:
'''You can take a part of a string by slicing it, meaning you extract a section of the string.'''
greeting = "Hello, World!"
print(greeting[0:5])  # Output: Hello

# Strings Can Be Concatenated: 
'''You can combine (join) two strings together using the + operator.'''
first_name = "Alice"
last_name = "Sam"
full_name = first_name + " " + last_name
print(full_name)  # Output: Alice Sam

# Strings Have Useful Functions: 
'''Python provides several built-in functions to work with strings, such as len() to find the length of a string, upper() to convert the string to uppercase, and lower() to convert the string to lowercase.'''
text = "Python is fun!"
print(len(text))  # Output: 14
print(text.upper())  # Output: PYTHON IS FUN!
print(text.lower())  # Output: python is fun!

# Types of Strings in Python:
# Single-line Strings: 
'''These are strings that are written on one line.'''
greeting = "Hello"

# Multi-line Strings: 
'''These are strings that span across multiple lines. You can create a multi-line string by using triple quotes''' # ('''...''' or """...""").
message = """This is a 
multi-line 
string."""

# Raw Strings: 
'''Sometimes you don’t want special characters (like \n for new line) to be treated specially. In such cases, you can use raw strings by adding an r before the quotes.'''
raw_string = r"C:\new_folder"
print(raw_string)  # Output: C:\new_folder

# The f in f-string stands for "formatted." 
'''You create an f-string by prefixing your string with the letter f or F, followed by the string in quotes, with any variables or expressions inside curly braces.'''
name = "Alice"
age = 10
print(f"My name is {name} and I am {age} years old.")

# Operations on Strings:
# Concatenation: 
'''Joining two or more strings using +.
Example: "Hello, " + "World!"'''

# Repetition: 
'''You can repeat a string multiple times using *.
Example: "Hello" * 3 will output "HelloHelloHello"'''

# Membership: 
'''You can check if a substring exists in a string using the in keyword.'''
if "Python" in "Python is fun!":
    print("Yes, it's there!")

# Common String Methods:
# upper(): 
'''Converts the string to uppercase.'''

# lower(): 
'''Converts the string to lowercase.'''

# strip(): 
'''Removes any whitespace from the beginning and end of the string.'''

# replace(): 
'''Replaces part of the string with another string.
Example: "Hello, World!".replace("World", "Python") will return "Hello, Python!"'''

# Asking for the user's favorite hobby
hobby = input("What is your favorite hobby? ")

# Printing the hobby in uppercase and its length
print("Your favorite hobby in uppercase: ", hobby.upper())
print("Length of your hobby: ", len(hobby))

# Checking if 'play' is in the hobby
if 'play' in hobby:
    print("You mentioned 'play' in your hobby!")








