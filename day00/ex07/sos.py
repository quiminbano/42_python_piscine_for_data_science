import sys


def main():
    """This function converts a string or a couple of them into Morse code"""
    NESTED_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
                    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--',
                    'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
                    'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
                    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                    'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
                    '3': '...--', '4': '....-', '5': '.....', '6': '-....',
                    '7': '--...', '8': '---..', '9': '----.', ' ': '/'}
    original_string = ""
    try:
        if len(sys.argv) != 2:
            raise AssertionError("AssertionError: the arguments are bad")
        original_string = sys.argv[1]
        capitalized_string = original_string.upper()
        flag = 0
        try:
            for char in capitalized_string:
                NESTED_MORSE[char]
        except KeyError:
            raise AssertionError("AssertionError: the arguments are bad")
    except AssertionError as e:
        print(e)
        sys.exit(1)
    flag = 0
    for char in capitalized_string:
        if flag == 0:
            flag = 1
        else:
            print(" ", end="")
        print(NESTED_MORSE[char], end="")
    print("")


if __name__ == "__main__":
    main()
