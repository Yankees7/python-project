"""Python Decorator Study"""

from functools import wraps


def decorator(func):
    """Decorator function to add functionality before and after the original function."""

    @wraps(func)  # This preserves the original function's metadata
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result

    return wrapper


@decorator
def say_hello(name):
    """Function to greet a person."""
    print(f"Hello, {name}!")
    return "Greeting completed."


if __name__ == "__main__":
    # Test the decorator
    result = say_hello("Alice")
    print(result)
    print(say_hello.__name__)  # This will still show 'wrapper' due to the decorator
