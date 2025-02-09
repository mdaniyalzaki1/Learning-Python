"""
Python Conditionals - A Detailed Explanation

This script covers:
- if statements
- if-else statements
- if-elif-else statements
- Nested conditionals
- Ternary operator
"""

# If Statement
age = 18
if age >= 18:
    print("You are an adult.")  # Executes if condition is True

# If-Else Statement
num = 10
if num % 2 == 0:
    print("Even number")  # Executes if condition is True
else:
    print("Odd number")  # Executes if condition is False

# If-Elif-Else Statement
grade = 85
if grade >= 90:
    print("A Grade")
elif grade >= 80:
    print("B Grade")
elif grade >= 70:
    print("C Grade")
else:
    print("Fail")

# Nested Conditionals
x = 10
y = 5
if x > y:
    if x % y == 0:
        print("x is a multiple of y")
    else:
        print("x is greater than y but not a multiple")

# Ternary Operator
status = "Adult" if age >= 18 else "Minor"
print("Status:", status)
