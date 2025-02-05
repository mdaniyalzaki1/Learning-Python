# data_types.py

# Numeric Types
num1 = 10          # int
num2 = 3.14        # float
num3 = 2 + 3j      # complex
print(f"num1: {num1}, num2: {num2}, num3: {num3}")

# String Type
name = "Alice"     # str
greeting = 'Hello!' # str
print(f"Name: {name}, Greeting: {greeting}")

# Boolean Type
is_active = True   # bool
is_sunny = False   # bool
print(f"is_active: {is_active}, is_sunny: {is_sunny}")

# Sequence Types
fruits = ['apple', 'banana', 'cherry']  # list
coordinates = (10, 20, 30)               # tuple
numbers = range(1, 10)                   # range
print(f"Fruits: {fruits}, Coordinates: {coordinates}, Numbers: {list(numbers)}")

# Mapping Type (Dictionary)
student = {"name": "Alice", "age": 20, "grade": "A"}  # dict
print(f"Student: {student}")

# Set Types
colors = {"red", "green", "blue"}        # set
immutable_colors = frozenset(["yellow", "black"])  # frozenset
print(f"Colors: {colors}, Immutable Colors: {immutable_colors}")

# Binary Types
byte_data = b"Hello"         # bytes
byte_array = bytearray(5)    # bytearray
print(f"Byte Data: {byte_data}, Byte Array: {byte_array}")

# None Type
data = None  # None
print(f"Data: {data}")

# Type Conversion
x = "10"
y = int(x)    # Convert string to integer
print(f"Converted string to int: {y}")

z = 3.14
w = str(z)    # Convert float to string
print(f"Converted float to string: {w}")
