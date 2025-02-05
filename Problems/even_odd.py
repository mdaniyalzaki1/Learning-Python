while True:
    number = int(input("Enter a Number (To Exit Enter : 0): "))

    if number == 0:
        print("Exiting the program.")
        break  # Exit the loop when user enters 0
    elif number < 0:
        print("Please Enter a Positive Integer")
    else:
        if number % 2 == 0:
            print(f"The number {number} is Even")
        else:
            print(f"The number {number} is Odd")
