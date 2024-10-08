# Lists and Tuples in Python
# 1. Lists
'''A list in Python is like a container where you can store multiple items. The items can be numbers, words, or any other type of data.'''
my_list = [10, 20, 30, "apple", True]  # A list with different types of data
print(my_list[0])  # Output: 10 (Accessing the first item)
my_list[1] = 50    # Changing the second item
print(my_list)     # Output: [10, 50, 30, "apple", True]

# Key Characteristics of Lists:
# Ordered: 
'''The items in a list have a specific order. You can access them using their position (index).'''

# Mutable: 
'''This means you can change the list after creating it. For example, you can add, remove, or modify items.'''

# Can store different types: 
'''A list can store numbers, strings, or even other lists.'''

# Indexed from 0: 
'''The first item in a list is at index 0, the second at index 1, and so on.'''

# Types of Lists:
# Empty list: 
'''A list with no items.'''
my_list = []

# List with same type of items: 
'''All items in the list are of the same type.'''
numbers = [1, 2, 3, 4]

# List with different types of items: 
'''A list can store a mix of different data types.'''
mixed = [1, "apple", 3.14, True]

# Nested list: 
'''A list within another list.'''
nested = [[1, 2], [3, 4], [5, 6]]

# Common List Methods:
# append(item): 
'''Adds an item to the end of the list.'''
my_list = [1, 2, 3]
my_list.append(4)  # List becomes [1, 2, 3, 4]

# insert(index, item): 
'''Inserts an item at a specific position.'''
my_list = [1, 3, 4]
my_list.insert(1, 2)  # List becomes [1, 2, 3, 4]

# remove(item): 
'''Removes the first occurrence of an item from the list.'''
my_list = [1, 2, 3, 2]
my_list.remove(2)  # List becomes [1, 3, 2] (removes the first 2)

# pop(index): 
'''Removes and returns the item at the given index (if no index is provided, removes the last item).'''
my_list = [1, 2, 3]
my_list.pop()  # Removes and returns 3, list becomes [1, 2]

# sort(): 
'''Sorts the list in ascending order.'''
my_list = [3, 1, 2]
my_list.sort()  # List becomes [1, 2, 3]

# reverse(): 
'''Reverses the order of items in the list.'''
my_list = [1, 2, 3]
my_list.reverse()  # List becomes [3, 2, 1]

# index(item): 
'''Returns the index of the first occurrence of an item.'''
my_list = [1, 2, 3]
print(my_list.index(2))  # Output: 1

# count(item): 
'''Returns the number of times an item appears in the list.'''
my_list = [1, 2, 2, 3]
print(my_list.count(2))  # Output: 2

# 2. Tuples
'''A tuple is similar to a list, but there’s one major difference: tuples cannot be changed after they are created.'''
my_tuple = (10, 20, 30, "banana", False)  # A tuple with different types of data
print(my_tuple[0])  # Output: 10 (Accessing the first item)
# my_tuple[1] = 50  # This will cause an error because tuples can't be changed

# Key Characteristics of Tuples:

# Ordered: 
'''Just like lists, tuples also have an order, and you can access items using their index.'''

# Immutable: 
'''Once a tuple is created, it cannot be changed.'''

# Can store different types: 
'''Like lists, tuples can also hold numbers, strings, or other types of data.'''

# Indexed from 0: 
'''The first item in a tuple is at index 0.'''

# Types of Tuples:
# Empty tuple: 
'''A tuple with no items.'''
my_tuple = ()

# Tuple with one item: 
'''For single-item tuples, you need to include a comma.'''
one_item = (5,)

# Tuple with multiple items: 
'''A tuple with more than one item.'''
my_tuple = (1, 2, "banana", False)

# Common Tuple Methods:
# count(item): 
'''Returns the number of times an item appears in the tuple.'''
my_tuple = (1, 2, 2, 3)
print(my_tuple.count(2))  # Output: 2

# index(item): 
'''Returns the index of the first occurrence of an item.'''
my_tuple = (1, 2, 3)
print(my_tuple.index(2))  # Output: 1


# Differences Between Lists and Tuples:
'''Feature	           Lists	                                  Tuples
Mutability	           Mutable (can be changed)                   Immutable (cannot be changed)
Syntax	               [ ]	                                      ( )
Performance	           Slower	                                  Faster
Use cases	           When you need to change data	              When data should remain constant'''




