import time
from functools import wraps

def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.2f}s")
        return result
    return wrapper


def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"{func.__name__} has been called {wrapper.calls} times")
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


@count_calls
def say_hello(name):
    print(f"Hello, {name}!!!!!!!!!!")


#  Random Names
say_hello("Alice")
say_hello("Bob")
say_hello("Charlie")