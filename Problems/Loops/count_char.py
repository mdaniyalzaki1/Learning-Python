# Define a string variable with a name
name = "M.Daniyal Zaki"

# Loop through unique characters using set()
for char in set(name):
    print(f"'{char}' appears {name.count(char)} times")
