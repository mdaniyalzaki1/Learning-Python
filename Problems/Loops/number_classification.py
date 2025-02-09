# List of numbers
numbers = [1, 2, -5, 7, -8, -2, -9, 6, 3]

# Variables to count positive and negative numbers
positive_number = 0
negative_numbers = 0

# Loop through each number in the list
for i in numbers:
    if i > 0:  # Check if the number is positive
        print("positive: ", i)
        positive_number += 1  # Increment the positive count
    elif i < 0:  # Check if the number is negative
        print("negative: ", i)
        negative_numbers += 1  # Increment the negative count

# Print the total count of positive and negative numbers
print("Total positive numbers: ", positive_number)
print("Total negative numbers: ", negative_numbers)
