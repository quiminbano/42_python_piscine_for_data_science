class ft_filter:
    __doc__ = """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    def __init__(self, function: any, iterable):
        """This function initializes the ft_filter class object with the\
 function and iterable arguments. The function argument is optional"""
        self.__type_name = type(iterable).__name__
        if hasattr(iterable, "__iter__") is False:
            raise TypeError(f"'{self.__type_name}' object is not iterable")
        self.__function = function
        if callable(self.__function) is False and function is not None:
            return None
        elif function is None:
            self.__result = iterable
        else:
            if isinstance(iterable, list) or isinstance(iterable, str):
                self.__result = [x for x in iterable if function(x)]
            elif isinstance(iterable, dict):
                self.__result = {
                    x: y for x, y in iterable.items() if function(x, y)
                    }
            elif isinstance(iterable, set):
                self.__result = {x for x in iterable if function(x)}
            elif isinstance(iterable, tuple):
                self.__result = tuple(x for x in iterable if function(x))
            else:
                raise TypeError(f"'{self.__type_name}' type not supported")

    def __iter__(self):
        """This function returns the iterator object of the ft_filter class"""
        function_type = type(self.__function).__name__
        if callable(self.__function) is False and self.__function is not None:
            raise TypeError(f"'{function_type}' object is not callable")
        return iter(self.__result)

    def __repr__(self):
        """This function returns the string representation of the ft_filter\
 class object"""
        return f"<ft_filter object at {hex(id(self))}>"
