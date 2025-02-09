"""
Python Lists - A Detailed Explanation

This script covers:
- Creating lists
- Accessing elements
- List slicing
- Modifying lists
- Iterating through lists
- Nesting lists
"""

# Creating Lists
empty_list = []  # An empty list
numbers = [1, 2, 3, 4, 5]  # A list of numbers
mixed_list = [1, "Hello", 3.5, True]  # A list with different data types
nested_list = [[1, 2, 3], [4, 5, 6]]  # A nested list

print("Lists:", numbers, mixed_list, nested_list)

# Accessing Elements
print("First Element:", numbers[0])  # Accessing first element
print("Last Element:", numbers[-1])  # Accessing last element

# List Slicing
print("Slice from index 1 to 3:", numbers[1:4])  # Slicing (start:stop)
print("Every second element:", numbers[::2])  # Slicing with step

# Modifying Lists
numbers.append(6)  # Appends element to the end
numbers.insert(2, 10)  # Inserts element at index 2
numbers[0] = 99  # Modifies element at index 0
print("Modified List:", numbers)

# Iterating Through a List
for num in numbers:
    print("Number:", num)

# Nesting Lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Nested List Element:", matrix[1][1])  # Accessing nested list element
