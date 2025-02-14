import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"The function starts in {start} and ends in {end}")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)

example_function(2)
