import time  # Import the time module for delay

# Initialize an empty list to store numbers
num_list = []

# Infinite loop to keep asking for input until the user exits
while True:
    try:
        # Take user input as an integer
        n = int(input("Enter a number (0 to Exit): "))

        # Exit condition if the user enters 0
        if n == 0:
            print("Exiting the program...")
            time.sleep(3)  # Wait for 3 seconds before exiting
            print("\nGoodbye!")
            break  # Exit the loop

        # Append the entered number to the list
        num_list.append(n)

        # Check if the entered number is between 1 and 10
        if 1 <= n <= 10:
            while True:  # Loop until valid input is received
                try:
                    decision = int(
                        input("Do you want to Exit or see all numbers you have entered?\n(0 to Exit, 1 to Print): "))

                    if decision == 0:  # If the user chooses to exit
                        print("Exiting the program...")
                        time.sleep(3)
                        print("\nGoodbye!")
                        exit()  # Use exit() to terminate the program

                    elif decision == 1:  # If the user wants to print the entered numbers
                        print(f"The list of numbers is: {num_list}")  # Display the list
                        break  # Exit the inner loop

                    else:
                        print("Invalid choice. Please enter 0 to Exit or 1 to Print.")

                except ValueError:
                    print("Invalid input! Please enter a number (0 or 1).")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")
