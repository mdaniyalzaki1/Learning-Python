while True:
    year = int(input("Enter the Year (0 to exit): "))  # Ask for input inside the loop

    if year == 0:  # Exit condition
        print("Exiting the program.")
        break

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a Leap Year")
    else:
        print(f"{year} is NOT a Leap Year")
