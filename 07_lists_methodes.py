"""
Python List Methods - A Comprehensive Guide

This script covers:
- Commonly used list methods and their usage
"""

# Sample list for demonstration
sample_list = [1, 2, 3, 4, 5]
print(sample_list)
# Commonly Used List Methods
sample_list.append(6)  # Adds an element to the end
print("After append:", sample_list)

sample_list.insert(2, 10)  # Inserts element at a specific index
print("After insert:", sample_list)

sample_list.remove(3)  # Removes the first occurrence of a value
print("After remove:", sample_list)

popped_element = sample_list.pop()  # Removes and returns the last element
print("After pop:", sample_list, "Popped Element:", popped_element)

index_of_4 = sample_list.index(4)  # Finds the index of a value
print("Index of 4:", index_of_4)

count_of_2 = sample_list.count(2)  # Counts occurrences of a value
print("Count of 2:", count_of_2)

sample_list.reverse()  # Reverses the list
print("After reverse:", sample_list)

sample_list.sort()  # Sorts the list in ascending order
print("After sort:", sample_list)

sample_list.clear()  # Clears all elements from the list
print("After clear:", sample_list)
