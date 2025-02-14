def sum_of_numbers(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return sum(result)
    return wrapper

@sum_of_numbers
def numbers():
    num = input("Enter numbers separated by , : ")
    return [int(n) for n in num.split(",")]

print(numbers())
