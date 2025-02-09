"""
Python Tuples - A Detailed Explanation

This script covers:
- Creating tuples
- Accessing elements
- Tuple slicing
- Tuple immutability
- Iterating through tuples
- Nested tuples
"""

# Creating Tuples
empty_tuple = ()  # An empty tuple
single_element_tuple = (5,)  # A tuple with a single element (comma is necessary)
numbers = (1, 2, 3, 4, 5)  # A tuple of numbers
mixed_tuple = (1, "Hello", 3.5, True)  # A tuple with different data types
nested_tuple = ((1, 2), (3, 4), (5, 6))  # A tuple containing tuples

print("Tuples:", numbers, mixed_tuple, nested_tuple)

# Accessing Elements
print("First Element:", numbers[0])  # Accessing first element
print("Last Element:", numbers[-1])  # Accessing last element

# Tuple Slicing
print("Slice from index 1 to 3:", numbers[1:4])  # Slicing (start:stop)
print("Every second element:", numbers[::2])  # Slicing with step

# Tuple Immutability
# numbers[0] = 10  # Uncommenting this line will raise an error since tuples are immutable

# Iterating Through a Tuple
for item in mixed_tuple:
    print("Item:", item)

# Nested Tuples
print("Nested Tuple Element:", nested_tuple[1][0])  # Accessing nested tuple elements
