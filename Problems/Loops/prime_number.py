# Import necessary modules
import time  # Used to pause execution before exiting
import math  # Used to calculate the square root for prime checking

# Infinite loop to repeatedly ask for user input
while True:
    # Prompt user to enter a number
    num = int(input("Enter a number (0 to EXIT):"))

    # Check if the user wants to exit
    if num == 0:
        print("Exiting the Program...")
        time.sleep(3)  # Pause for 3 seconds before exiting
        print("GoodBye!")
        break  # Exit the loop

    # Check if the number is prime
    if num < 2:  
        is_prime = False  # Numbers less than 2 are not prime
    else:
        is_prime = True  # Assume the number is prime initially
        # Loop from 2 to the square root of the number (inclusive)
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:  # If the number is divisible by i, it's not prime
                is_prime = False
                break  # Exit the loop early since we found a divisor

    # Print the result
    if is_prime:
        print(f"The number {num} is 'PRIME'")
    else:
        print(f"The number {num} is 'NOT PRIME'")
