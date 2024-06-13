class calculator:
    def __init__(self, vector) -> None:
        self.__vector = vector

    def __add__(self, object) -> None:
        temp = [(x + object) for x in self.__vector]
        self.__vector = temp
        print(self.__vector)

    def __sub__(self, object) -> None:
        temp = [(x - object) for x in self.__vector]
        self.__vector = temp
        print(self.__vector)

    def __mul__(self, object) -> None:
        temp = [(x * object) for x in self.__vector]
        self.__vector = temp
        print(self.__vector)

    def __truediv__(self, object) -> None:
        try:
            temp = [(x / object) for x in self.__vector]
            self.__vector = temp
            print(self.__vector)
        except ZeroDivisionError:
            print("Division by Zero: I can't do that operation")
