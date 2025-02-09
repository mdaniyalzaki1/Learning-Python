"""
Python String Methods - A Comprehensive Guide

This script covers:
- Common string methods and their usage
"""

# Sample text for demonstration
sample_text = "  Hello, Python!  "

# Commonly Used String Methods
print("Lowercase:", sample_text.lower())  # Converts to lowercase
print("Uppercase:", sample_text.upper())  # Converts to uppercase
print("Title Case:", sample_text.title())  # Converts to title case
print("Stripped:", sample_text.strip())  # Removes leading/trailing spaces
print("Replaced:", sample_text.replace("Python", "World"))  # Replaces substring
print("Split:", sample_text.split(","))  # Splits string into list
print("Joined:", "-".join(["Python", "Programming"]))  # Joins elements with a separator
print("Find position of 'Python':", sample_text.find("Python"))  # Finds index of substring
print("Count occurrences of 'l':", sample_text.count("l"))  # Counts occurrences of character
print("Starts with 'Hello':", sample_text.startswith("H"))  # Checks start of string
print("Ends with '!':", sample_text.endswith("!"))  # Checks end of string
