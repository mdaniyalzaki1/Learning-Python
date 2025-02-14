# Function for basic arithmetic operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

def remainder(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a % b

def power(a, b):
    return a ** b

def root(a, b):
    return a ** (1 / b)

def square(a):
    return a ** 2

def cube(a):
    return a ** 3

# Display menu options
print("What operation would you like to perform?")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Remainder (Modulo)")
print("6. Power (Exponentiation)")
print("7. Root")
print("8. Square")
print("9. Cube")

try:
    # Get user choice
    choice = int(input("Enter your choice (1-9): "))

    # If choice is valid, proceed
    if choice in range(1, 10):
        # For Square and Cube, we only need one input
        if choice in [8, 9]:
            num1 = float(input("Enter the number: "))
            num2 = None  # Not needed for square/cube
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

        # Perform the chosen operation
        if choice == 1:
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif choice == 2:
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == 3:
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif choice == 4:
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
        elif choice == 5:
            result = remainder(num1, num2)
            print(f"{num1} % {num2} = {result}")
        elif choice == 6:
            result = power(num1, num2)
            print(f"{num1} ^ {num2} = {result}")
        elif choice == 7:
            result = root(num1, num2)
            print(f"{num1} root {num2} = {result}")
        elif choice == 8:
            result = square(num1)
            print(f"{num1}² = {result}")
        elif choice == 9:
            result = cube(num1)
            print(f"{num1}³ = {result}")

    else:
        print("Invalid choice! Please enter a number between 1 and 9.")

except ValueError:
    print("Invalid input! Please enter a number.")
