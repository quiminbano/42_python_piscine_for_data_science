def print_result(value: str, temp_list: list, length) -> None:
    copy = temp_list
    if isinstance(value, str) is False:
        return None
    mean = (sum(copy) / length)
    if length % 2 == 0:
        median = ((copy[length // 2] + copy[length // 2 - 1]) / 2)
    else:
        median = copy[length // 2]
    if value == "mean":
        print(f"Mean : {mean}")
    elif value == "median":
        print(f"Median : {median}")


def ft_statistics(*args: any, **kwargs: any) -> None:
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
