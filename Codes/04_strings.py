"""
Python Strings - A Detailed Explanation

This script covers:
- Creating and defining strings
- String indexing and slicing
- String formatting
- Escape sequences
- Multi-line strings
"""

# Creating Strings
single_quote_str = 'Hello'  # Using single quotes
double_quote_str = "Hello"  # Using double quotes
triple_quote_str = '''Hello'''  # Using triple quotes for multi-line strings
print(single_quote_str, double_quote_str, triple_quote_str)

# String Indexing and Slicing
string_sample = "Python Programming"
print("First Character:", string_sample[0])  # Accessing first character
print("Last Character:", string_sample[-1])  # Accessing last character
print("Substring:", string_sample[0:6])  # Slicing (start:stop)
print("Every second character:", string_sample[::2])  # Slicing with step
print("Reversed String:", string_sample[::-1])  # Reversing a string

# String Formatting
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")  # f-string formatting
print("My name is {} and I am {} years old.".format(name, age))  # format() method
print("My name is %s and I am %d years old." % (name, age))  # Old-style formatting

# Escape Sequences
print("Line Break:\nNew Line")  # Newline character
print("Tab Space:\tIndented")  # Tab character
print("Quotes: \"Python\" is fun")  # Escape double quotes

# Multi-line Strings
multi_line_str = """This is a multi-line string.
It spans multiple lines."""
print(multi_line_str)
