# Conditional Expressions in Python
'''Conditional expressions are used to perform different actions or calculations based on certain conditions.'''
marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: D")

# Types of Conditional Statements
# if Statement: 
'''The if statement checks if a condition is true. If the condition is true, it runs the block of code inside the if. If the condition is false, it skips this block.'''
age = 18
if age >= 18:
    print("You are eligible to vote.")

# elif Statement (short for "else if"): 
'''The elif statement allows you to check multiple conditions. If the first if condition is false, it checks the elif condition. If this is true, it executes the code inside elif.'''
age = 16
if age >= 18:
    print("You are eligible to vote.")
elif age >= 16:
    print("You are eligible to get a driving license.")

# else Statement: 
'''The else statement catches anything that doesn’t meet the conditions of the if or elif statements. It runs when all previous conditions are false.'''
age = 12
if age >= 18:
    print("You are eligible to vote.")
elif age >= 16:
    print("You are eligible to get a driving license.")
else:
    print("You are too young for both.")

# Nested if Statements: 
'''You can place an if statement inside another if statement to create more complex logic.'''
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("You can enter the club.")
    else:
        print("You need an ID to enter.")
else:
    print("You are too young to enter.")

# Ternary (Conditional) Operator: 
'''This is a one-liner if-else expression. It's useful for short conditions.'''
age = 17
status = "Adult" if age >= 18 else "Minor"
print(status)

# Characteristics of Conditional Statements
# Flow Control: 
'''Conditional statements control the flow of your program by executing certain parts of the code depending on whether a condition is true or false.'''

# Boolean Logic: 
'''Conditions in if statements rely on boolean values (True or False). These conditions often involve comparisons (like ==, >, <, etc.).'''

# Flexible: 
'''Python allows you to combine multiple conditions using logical operators such as and, or, and not.'''

# Nested Statements: 
'''you can nest if, elif, and else statements within each other to handle complex scenarios.'''

# Indentation: 
'''Python uses indentation (spaces or tabs) to define the code inside each condition. It is important to ensure consistent indentation.'''

