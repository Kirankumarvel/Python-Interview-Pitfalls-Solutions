def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def greet():
    print("Hello!")

greet()

# Pitfall: decorators that lose function metadata
print(greet.__name__)  # Outputs 'wrapper', not 'greet'

# Fix with functools.wraps
import functools

def better_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@better_decorator
def greet2():
    print("Hello again!")

greet2()
print(greet2.__name__)  # Outputs 'greet2'
