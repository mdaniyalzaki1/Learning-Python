# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(temp):
    return (temp * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(temp):
    return (temp - 32) * 5/9

# Function to convert Celsius to Kelvin
def celsius_to_kelvin(temp):
    return temp + 273.15

# Function to convert Kelvin to Celsius
def kelvin_to_celsius(temp):
    return temp - 273.15

# Function to convert Kelvin to Fahrenheit
def kelvin_to_fahrenheit(temp):
    return (temp - 273.15) * 9/5 + 32

# Function to convert Fahrenheit to Kelvin
def fahrenheit_to_kelvin(temp):
    return (temp - 32) * 5/9 + 273.15

# Infinite loop to keep the program running until the user chooses to exit
while True:
    # Display the menu options
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Kelvin to Fahrenheit")
    print("6. Fahrenheit to Kelvin")
    print("7. Exit")

    try:
        # Prompt user to choose an option
        choice = int(input("Enter your choice (1-7): "))

        # If the user chooses to exit, break the loop
        if choice == 7:
            print("Exiting the program. Goodbye!")
            break  # Exit without asking for temperature

        # Prompt user to enter a temperature value
        temp = float(input("Enter the temperature: "))

        # Perform the selected conversion based on user choice
        if choice == 1:
            result = celsius_to_fahrenheit(temp)
            print(f"{temp}°C is equal to {result:.2f}°F")
        elif choice == 2:
            result = fahrenheit_to_celsius(temp)
            print(f"{temp}°F is equal to {result:.2f}°C")
        elif choice == 3:
            result = celsius_to_kelvin(temp)
            print(f"{temp}°C is equal to {result:.2f}K")
        elif choice == 4:
            result = kelvin_to_celsius(temp)
            print(f"{temp}K is equal to {result:.2f}°C")
        elif choice == 5:
            result = kelvin_to_fahrenheit(temp)
            print(f"{temp}K is equal to {result:.2f}°F")
        elif choice == 6:
            result = fahrenheit_to_kelvin(temp)
            print(f"{temp}°F is equal to {result:.2f}K")
        else:
            print("Invalid choice! Please enter a number between 1 and 7.")
            continue  # Skip printing the result if choice is invalid

    except ValueError:
        # Handle non-numeric input gracefully
        print("Invalid input! Please enter a valid number.")
