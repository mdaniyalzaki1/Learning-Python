import random
import string

print("LOGIN")

gmail = input("Enter Your Google Mail: ")
print("Would you like to Write your own password or We generate a Strong Password?")
choiceuser = int(input("Enter your choice (1 for own, 0 for Strong): "))

if choiceuser == 1:
    passworduser = input("Enter your Password: ")
    print(f"Your Username is {gmail} \nYour Password is {passworduser}")
elif choiceuser == 0:
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random string of length 10
    genpassword = ''.join(random.choice(characters) for _ in range(10))
    print(f"Your Username is {gmail} \nYour Password is {genpassword}")
else:
    print("Invalid choice. Please enter 0 or 1.")

print("Thankyou!")
