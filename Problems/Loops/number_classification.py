numbers = [1, 2, -5, 7, -8, -2, -9, 6, 3]

positive_number = 0
negative_numbers = 0

for i in numbers:
    if i > 0:
        print("positive: ", i)
        positive_number += 1
    elif i < 0:
        print("negative: ", i)
        negative_numbers +=1

print("Total positive numbers: ", positive_number)
print("Total negative numbers: ", negative_numbers)