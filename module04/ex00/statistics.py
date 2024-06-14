def get_mean(copy: list, length: int) -> float:
    """This function returns the mean of the list passed as an argument"""
    return (sum(copy) / length)


def get_median(copy: list, length: int) -> float:
    """This function returns the median of the list passed as an argument"""
    copy.sort()
    if length % 2 == 0:
        return ((copy[length // 2] + copy[length // 2 - 1]) / 2)
    else:
        return copy[length // 2]


def get_std(copy: list, length: int) -> float:
    """This function returns the standard deviation of the list passed as an\
 argument"""
    mean = get_mean(copy, length)
    return (sum((x - mean) ** 2 for x in copy) / length) ** 0.5


def get_var(copy: list, length: int) -> float:
    """This function returns the variance of the list passed as an argument"""
    mean = get_mean(copy, length)
    return sum((x - mean) ** 2 for x in copy) / length


def get_quartile(copy: list, length: int) -> tuple:
    """This function returns the quartile of the list passed as an argument"""
    copy.sort()
    lower_length = (length // 4)
    upper_length = ((length // 4) * 3)
    if length % 4 == 0:
        lower_quartile = (copy[lower_length] + copy[lower_length - 1]) / 2
    else:
        lower_quartile = copy[lower_length]
    if (length * 3) % 4 == 0:
        upper_quartile = (copy[upper_length] + copy[upper_length - 1]) / 2
    else:
        upper_quartile = copy[upper_length]
    return [float(lower_quartile), float(upper_quartile)]


def print_result(value: str, temp_list: list, length) -> None:
    """This function prints the result of the statistics function required \
by the user coming from ft_statistics function."""
    copy = temp_list
    if isinstance(value, str) is False:
        return None
    match value:
        case "mean":
            print(f"mean : {get_mean(copy, length)}")
        case "median":
            print(f"median : {get_median(copy, length)}")
        case "std":
            print(f"std : {get_std(copy, length)}")
        case "var":
            print(f"var : {get_var(copy, length)}")
        case "quartile":
            print(f"quartile: {get_quartile(copy, length)}")
        case _:
            pass


def ft_statistics(*args: any, **kwargs: any) -> None:
    """This function takes in a list of numbers and a string as arguments and \
returns the statistics of the list of numbers based on the string passed as \
an argument. The string can be either mean, median, std, variance, or \
quartile."""
    temp_list = []
    try:
        assert len(kwargs) != 0, "ERROR"
    except AssertionError as e:
        print(e)
        return None
    try:
        assert len(args) != 0, "ERROR"
        length = len(args)
        for arg in args:
            assert isinstance(arg, (int, float)), "ERROR"
            temp_list.append(arg)
        for key, value in kwargs.items():
            key = key
            print_result(value, temp_list, length)
    except AssertionError as e:
        for x, y in kwargs.items():
            x = x
            y = y
            print(e)
