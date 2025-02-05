"""
Python Numbers

This script covers:
- Integer, Float, and Complex numbers
- Arithmetic operations
- Type conversions
- Built-in functions related to numbers
- Number representations (binary, octal, hexadecimal)
"""

# Integer (int)
int_num = 10  # A whole number, positive or negative, without decimals
print("Integer:", int_num, "Type:", type(int_num))

# Float (float)
float_num = 10.5  # A number with a decimal point
print("Float:", float_num, "Type:", type(float_num))

# Complex (complex)
complex_num = 3 + 4j  # A number with a real and imaginary part
print("Complex:", complex_num, "Type:", type(complex_num))

# Type Conversion
converted_int = int(float_num)  # Converts float to int (removes decimal part)
converted_float = float(int_num)  # Converts int to float
converted_complex = complex(int_num)  # Converts int to complex
print("Converted int:", converted_int, "Converted float:", converted_float, "Converted complex:", converted_complex)

# Arithmetic Operations
sum_result = int_num + float_num  # Addition
sub_result = int_num - float_num  # Subtraction
mul_result = int_num * float_num  # Multiplication
div_result = int_num / float_num  # Division (returns float)
floor_div_result = int_num // float_num  # Floor division (discards decimal)
mod_result = int_num % 3  # Modulus (remainder)
exp_result = int_num ** 2  # Exponentiation

print("Arithmetic Operations:", sum_result, sub_result, mul_result, div_result, floor_div_result, mod_result, exp_result)

# Number Representations
binary_num = 0b1010  # Binary (prefix 0b)
octal_num = 0o12  # Octal (prefix 0o)
hex_num = 0xA  # Hexadecimal (prefix 0x)
print("Binary:", binary_num, "Octal:", octal_num, "Hexadecimal:", hex_num)
