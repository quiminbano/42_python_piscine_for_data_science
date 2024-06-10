from ft_filter import ft_filter
import sys


def main():
    """This function tests the implementation of ft_filter class with a lambda
function and a list comprehension applied to a ft_filter object"""


string_input = ""
try:
    if len(sys.argv) != 3:
        raise AssertionError("AssertionError: the arguments are bad")
    try:
        number_input = int(sys.argv[2])
    except ValueError:
        raise AssertionError("AssertionError: the arguments are bad")
    try:
        string_input = int(sys.argv[1])
        raise AssertionError("AssertionError: the arguments are bad")
    except ValueError:
        pass
except AssertionError as e:
    print(e)
    sys.exit(1)
string_input = sys.argv[1]
splitted_words = string_input.split()
try:
    result = ft_filter(lambda x: len(x) > number_input, splitted_words)
    result_list = [x for x in result]
    print(result_list)
except TypeError as e:
    print(e)
    sys.exit(1)


if __name__ == "__main__":
    main()
