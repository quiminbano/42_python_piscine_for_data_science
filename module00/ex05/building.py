import sys


def get_punt(text) -> bool:
    """This function will return the number of punctuation marks in a given\
 text"""
    return sum([1 for x in text if not str.isalnum(x) and not str.isspace(x)])


def main():
    """This function will count the different types of characters in a given\
 text"""
    sys.argv
    text_input = ""
    try:
        if len(sys.argv) > 2:
            raise AssertionError("AssertionError: Too many arguments")
        if len(sys.argv) != 1:
            text_input = sys.argv[1]
        else:
            try:
                print("What is the text to count?")
                text_input = sys.stdin.readline()
            except (EOFError, KeyboardInterrupt):
                raise AssertionError("AssertionError: Process interrupted")
    except AssertionError as e:
        print(e)
        sys.exit(1)
    upper_letters = sum(map(str.isupper, text_input))
    lower_letters = sum(map(str.islower, text_input))
    spaces = sum(map(str.isspace, text_input))
    digits = sum(map(str.isdigit, text_input))
    puntuation = get_punt(text_input)
    print("The text contains", len(text_input), "characters:")
    print(f"{upper_letters} upper letters")
    print(f"{lower_letters} lower letters")
    print(f"{puntuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


if __name__ == "__main__":
    main()
