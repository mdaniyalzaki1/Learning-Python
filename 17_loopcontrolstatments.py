"""
Python Loop Control Statements - A Detailed Explanation

This script covers:
- Using break, continue, and pass statements in loops
"""

# Break Statement
for num in range(10):
    if num == 5:
        break  # Exits the loop when num is 5
    print("Number:", num)

# Continue Statement
for num in range(5):
    if num == 2:
        continue  # Skips the iteration when num is 2
    print("Number:", num)

# Pass Statement
for num in range(3):
    if num == 1:
        pass  # Placeholder for future code
    print("Number:", num)
