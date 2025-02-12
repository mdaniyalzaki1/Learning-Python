import random  # Importing the random module for generating random numbers

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

# Introductory messages for the user
print("\tWelcome to Guess Number Game")
print("I have chosen a number between 1 and 100. Can you guess it?")

# Initialize the number of attempts made by the user
attempts = 0

# Loop to allow the user a maximum of 3 attempts to guess the number
while attempts < 3:
    # Prompt the user to enter their guess and convert it to an integer
    guess = int(input("Enter a number: "))

    # Increment the attempt count
    attempts += 1

    # Check if the user's guess matches the random number
    if guess == random_number:
        print(f"Congratulations! You've guessed the number in {attempts} attempts.")
        break  # Exit the loop if the user guesses correctly
    # Provide a hint if the guess is too low
    elif guess < random_number:
        print("Too low! Try again.")
    # Provide a hint if the guess is too high
    else:
        print("Too high! Try again.")

    # Notify the user of how many attempts have been made
    print(f"Attempt {attempts}/3")

    # If the user has used all 3 attempts without guessing correctly
    if attempts == 3 and guess != random_number:
        # Reveal the correct number and end the game
        print(f"Sorry! You lost. The correct number was {random_number}.")
# Losing message if all attempts are used
    if attempts == 3 and guess != random_number:
        print(f"Sorry! You lost. The correct number was {random_number}.")
