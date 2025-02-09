import time

print("\t---Multiplication Table Printer---")

while True:  # Infinite loop to keep asking for input
    num = int(input("Enter a number (0 to exit): "))  # Take user input

    if num == 0:  # Check if the user wants to exit
        print("Exiting the program...")
        time.sleep(3)  # Wait for 3 seconds before exiting
        print("\nGoodBye!")  # Add a newline for better formatting
        break  # Exit the loop

    num = abs(num)  # Convert negative numbers to positive

    # Print the multiplication table from 1 to 12
    for i in range(1, 13):
        print(f"{num} x {i} = {num * i}")

    print("-" * 30)  # Print a separator for clarity
