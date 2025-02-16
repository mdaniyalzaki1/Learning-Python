def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)  # Fixed variable name
        kwargs_value = ', '.join(f"{k} = {v}" for k, v in kwargs.items())
        print(f"Calling {func.__name__} with Args: {args_value}, Kwargs: {kwargs_value}")  # Fixed formatting
        return func(*args, **kwargs)
    return wrapper  # Missing return statement for the decorator

@debug
def greet(name, greeting="Hello"):
    return f"{greeting} {name}"

print(greet("Abdullah"))
