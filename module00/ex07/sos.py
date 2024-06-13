import sys


def main():
    """This function converts a string or a couple of them into Morse code"""
    NESTED_MORSE = {'A': '.- ', 'B': '-... ', 'C': '-.-. ', 'D': '-.. ',
                    'E': '. ', 'F': '..-. ', 'G': '--. ', 'H': '.... ',
                    'I': '.. ', 'J': '.--- ', 'K': '-.- ', 'L': '.-.. ',
                    'M': '-- ', 'N': '-. ', 'O': '--- ', 'P': '.--. ',
                    'Q': '--.- ', 'R': '.-. ', 'S': '... ', 'T': '- ',
                    'U': '..- ', 'V': '...- ', 'W': '.-- ', 'X': '-..- ',
                    'Y': '-.-- ', 'Z': '--.. ', '0': '----- ', '1': '.---- ',
                    '2': '..--- ', '3': '...-- ', '4': '....- ',
                    '5': '..... ', '6': '-.... ', '7': '--... ', '8': '---.. ',
                    '9': '----. ', ' ': '/ '}
    original_string = ""
    try:
        assert (len(sys.argv) == 2), "AssertionError: the arguments are bad"
        original_string = sys.argv[1]
        capitalized_string = original_string.upper()
        try:
            for char in capitalized_string:
                NESTED_MORSE[char]
        except KeyError:
            raise AssertionError("AssertionError: the arguments are bad")
    except AssertionError as e:
        print(e)
        sys.exit(1)
    temp_str = ""
    for char in capitalized_string:
        temp_str += NESTED_MORSE[char]
    temp_str = temp_str.rstrip()
    print(temp_str)


if __name__ == "__main__":
    main()
