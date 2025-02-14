"""
Python Functions - A Detailed Explanation

This script covers:
- What are functions?
- Types of functions in Python
- Defining and calling functions
- Function arguments and parameters
- Return values
- Lambda functions
"""

# What are Functions?
# Functions are reusable blocks of code that perform a specific task.

# Defining a Function
def greet():
    """A simple function that prints a greeting message."""
    print("Hello, welcome to Python functions!")

# Calling the function
greet()

# Function with Parameters
def add(a, b):
    """Function that takes two numbers and returns their sum."""
    return a + b

result = add(5, 3)
print("Sum:", result)

# Function with Default Parameters
def power(base, exponent=2):
    """Function that calculates the power of a number with a default exponent of 2."""
    return base ** exponent

print("Power:", power(3))  # Uses default exponent
print("Power:", power(3, 3))  # Uses given exponent

# Lambda Function
square = lambda x: x ** 2
print("Square of 4:", square(4))
