# Dictionaries and Sets in Python 
# Dictionary
'''A dictionary is a collection of items where each item is stored as a key-value pair. This means that every key has a corresponding value.'''

# Creating a dictionary
student = {
    "name": "Alice",
    "age": 10,
    "marks": 20
}

# Accessing value using key
print(student["name"])  # Output: Alice

# Adding a new key-value pair
student["subject"] = "Math"

# Updating a value
student["marks"] = 90

# Removing a key-value pair
del student["age"]

print(student)

# Characteristics of Dictionaries:
# Key-Value Pairs: 
'''Each element in a dictionary is a pair of a key and a value.''' 
{"name": "John", "age": 25}  #is a dictionary where "name" is a key, and "John" is its value.

# Unordered: 
'''Items in a dictionary are not stored in any particular order.'''

# Mutable: 
'''You can add, change, or remove elements in a dictionary after it is created.'''

# Keys are Unique: 
'''No two keys in a dictionary can be the same, but the values can be duplicated.'''

# Indexed by Keys: 
'''You use the key to access the value.'''

# Types of Dictionaries:
# Empty Dictionary: 
'''A dictionary without any items.'''
dictionary = {}

# Nested Dictionary: 
'''A dictionary within a dictionary.'''
students = {
    "student1": {"name": "John", "age": 25},
    "student2": {"name": "Jane", "age": 22}
}

# Common Dictionary Methods:
# dict.get(key): 
'''Returns the value for the specified key.'''

# dict.keys(): 
'''Returns all the keys in the dictionary.'''

# dict.values(): 
'''Returns all the values in the dictionary.'''

# dict.items(): 
'''Returns all key-value pairs as tuples.'''

# dict.update(): 
'''Adds or updates key-value pairs.'''

# dict.pop(key): 
'''Removes the item with the specified key and returns its value.'''

# Set
'''A set is a collection of unique items. Sets are great when you want to store elements and ensure there are no duplicates.'''

# Creating a set
fruits = {"apple", "banana", "cherry"}

# Adding an element to the set
fruits.add("orange")

# Removing an element from the set
fruits.remove("banana")

# Check if an element exists in the set
print("apple" in fruits)  # Output: True

print(fruits)

# Characteristics of Sets:
# Unordered: 
'''The elements in a set do not have a specific order.'''

# Unique Elements: 
'''A set cannot contain duplicate values.'''

# Mutable: 
'''You can add or remove items from a set.'''

# No Indexing: 
'''Sets do not support indexing or slicing like lists or dictionaries. You cannot access items by their position.'''

# Types of Sets:
# Empty Set: 
'''An empty set can only be created using set(). If you use {}, it will create an empty dictionary instead.'''

# Frozen Set: 
'''A frozen set is an immutable set. Once created, you cannot modify it.'''
frozen_set = frozenset([1, 2, 3])

# Common Set Methods:
# set.add(): 
'''Adds an element to the set.'''

# set.remove(): 
'''Removes an element from the set. If the element is not found, it raises an error.'''

# set.discard(): 
'''Removes an element from the set without raising an error if the element doesn't exist.'''

# set.union(): 
'''Combines two sets and removes duplicates.'''

# set.intersection(): 
'''Returns elements that are common in both sets.'''

# set.difference(): 
'''Returns the difference between two sets (elements that are only in the first set).'''







