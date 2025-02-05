num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
# print("Operations: \n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5. Reminder\n")
choice = input("Enter Operation(+,-,*,/,%):")

if choice == "+":
    result = num1 + num2
elif choice == "-":
    result = num1 - num2
elif choice == "*":
    result = num1 * num2
elif choice == "/":
    result = num1 / num2
elif choice == "%":
    result = num1 % num2
else:
    result = "Please Enter a Correct Choice(1-5)"

print(f"{num1} {choice} {num2} = {result}")

