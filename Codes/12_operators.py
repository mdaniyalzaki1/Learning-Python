"""
Python Operators - A Detailed Explanation

This script covers:
- Arithmetic Operators
- Comparison Operators
- Logical Operators
- Assignment Operators
- Membership Operators
- Identity Operators
"""

# Arithmetic Operators
a, b = 10, 3
print("Addition:", a + b)  # Adds two numbers
print("Subtraction:", a - b)  # Subtracts two numbers
print("Multiplication:", a * b)  # Multiplies two numbers
print("Division:", a / b)  # Performs division
print("Floor Division:", a // b)  # Division without remainder
print("Modulus:", a % b)  # Finds remainder
print("Exponentiation:", a ** b)  # Raises a to the power of b

# Comparison Operators
print("Equal:", a == b)  # Checks if a is equal to b
print("Not Equal:", a != b)  # Checks if a is not equal to b
print("Greater Than:", a > b)  # Checks if a is greater than b
print("Less Than:", a < b)  # Checks if a is less than b
print("Greater or Equal:", a >= b)  # Checks if a is greater or equal to b
print("Less or Equal:", a <= b)  # Checks if a is less or equal to b

# Logical Operators
x, y = True, False
print("AND Operator:", x and y)  # Returns True if both are True
print("OR Operator:", x or y)  # Returns True if at least one is True
print("NOT Operator:", not x)  # Reverses the boolean value

# Assignment Operators
c = 10
c += 5  # Equivalent to c = c + 5
print("After +=:", c)
c -= 3  # Equivalent to c = c - 3
print("After -=:", c)
c *= 2  # Equivalent to c = c * 2
print("After *=:", c)

# Membership Operators
text = "Hello Python"
print("'H' in text:", 'H' in text)  # Checks if 'H' is in the string
print("'z' not in text:", 'z' not in text)  # Checks if 'z' is not in the string

# Identity Operators
d = [1, 2, 3]
e = d
f = [1, 2, 3]
print("e is d:", e is d)  # True because e and d reference the same object
print("f is d:", f is d)  # False because f is a different object with the same content
print("f == d:", f == d)  # True because values are equal
