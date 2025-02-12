"""
Python While Loop - A Detailed Explanation

This script covers:
- Syntax of while loops
- Using conditions in while loops
- Avoiding infinite loops
"""

# While Loop Syntax
count = 0
while count < 5:
    print("Count:", count)
    count += 1  # Increment to avoid infinite loop

# Using a condition
number = 10
while number > 0:
    print("Number:", number)
    number -= 2
