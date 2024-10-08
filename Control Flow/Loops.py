# Loops in Python
# for Loop
'''A for loop is used when you know how many times you want to repeat a certain action.'''
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Characteristics of for loop:
'''It iterates over sequences (like lists or strings).
You know how many iterations will happen.
Commonly used when working with lists, ranges, or arrays.'''

# while Loop
'''A while loop continues to execute the block of code as long as a certain condition is True.'''
count = 0
while count < 5:
    print("Count is:", count)
    count += 1

# Characteristics of while loop:
'''It repeats the code until a condition is false.
Useful when the number of iterations is unknown.
Be careful with conditions, or you may end up with an infinite loop (which never stops).'''

# Loop Control Statements
# break Statement: 
'''This is used to exit the loop prematurely. When Python encounters a break, it stops the loop immediately.'''
for i in range(10):
    if i == 5:
        break
    print(i)

# continue Statement: 
'''This skips the rest of the loop’s code for the current iteration and moves to the next iteration.'''
for i in range(5):
    if i == 3:
        continue
    print(i)

# else in Loops: 
'''You can use an else block with loops. The code inside the else block is executed when the loop completes normally (without hitting a break).'''
for i in range(5):
    print(i)
else:
    print("Loop finished.")






