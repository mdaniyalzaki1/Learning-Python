import time

while True:
    n = int(input("Enter a number (0 to Exit): "))

    if n == 0:  # Exit condition
        print("Exiting the Program...")
        time.sleep(3)
        print("\nGoodBye!")
        break  # Exit the loop

    factorial = 1  # Reset factorial for each new input
    i = 1  # Initialize counter

    # Calculate factorial using while loop
    while i <= n:
        factorial *= i  # Multiply each number from 1 to n
        i += 1  # Increment counter

    print(f"Factorial of {n} is: {factorial}")
    print("-" * 30)  # Separator for better readability
