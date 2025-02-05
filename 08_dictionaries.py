"""
Python Dictionaries - A Detailed Explanation

This script covers:
- Creating dictionaries
- Accessing values
- Modifying dictionaries
- Iterating through dictionaries
- Nested dictionaries
"""

# Creating Dictionaries
empty_dict = {}  # An empty dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}  # Dictionary with key-value pairs

print("Dictionaries:", person)

# Accessing Values
print("Name:", person["name"])  # Access value by key
print("Age:", person.get("age"))  # Using get() method

# Modifying Dictionaries
person["age"] = 26  # Updating a value
person["gender"] = "Female"  # Adding a new key-value pair
print("Modified Dictionary:", person)

# Iterating Through a Dictionary
for key, value in person.items():
    print(key, "->", value)

# Removing Elements
del person["city"]  # Deleting a key-value pair
print("After Deletion:", person)

# Nested Dictionaries
students = {
    "student1": {"name": "Bob", "grade": "A"},
    "student2": {"name": "Emma", "grade": "B"}
}
print("Nested Dictionary:", students["student1"]["name"])  # Accessing nested values
