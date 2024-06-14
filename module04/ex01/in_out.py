def square(x: int | float) -> int | float:
    """This function return the square of a value passed as argument."""
    return x * x


def pow(x: int | float) -> int | float:
    """This function return the power of a value passed as argument."""
    return x ** x


def outer(x: int | float, function) -> object:
    """This function return a function that will apply the function passed as\
    argument to the value passed as argument."""
    count = 0

    def inner() -> float:
        nonlocal count
        y = x
        count += 1
        for i in range(count):
            y = function(y)
        return y
    return inner
