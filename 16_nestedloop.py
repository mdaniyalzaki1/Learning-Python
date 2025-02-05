"""
Python Nested Loops - A Detailed Explanation

This script covers:
- Using loops inside loops
- Iterating over multiple sequences
"""

# Nested For Loop
for i in range(3):
    for j in range(3):
        print(f"i: {i}, j: {j}")

# Nested While Loop
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i: {i}, j: {j}")
        j += 1
    i += 1
