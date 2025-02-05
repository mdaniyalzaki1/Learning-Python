"""
Python Dictionary Methods - A Comprehensive Guide

This script covers:
- Commonly used dictionary methods and their usage
"""

# Sample dictionary for demonstration
sample_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Commonly Used Dictionary Methods
print("Keys:", sample_dict.keys())  # Returns all keys
print("Values:", sample_dict.values())  # Returns all values
print("Items:", sample_dict.items())  # Returns all key-value pairs

sample_dict.update({"age": 26, "gender": "Female"})  # Updates dictionary with new values
print("After update:", sample_dict)

removed_value = sample_dict.pop("city")  # Removes a key and returns its value
print("After pop:", sample_dict, "Removed Value:", removed_value)

sample_dict.clear()  # Clears all elements from the dictionary
print("After clear:", sample_dict)
