from S1E9 import Character


class Baratheon(Character):
    __doc__ = """This children class represents the Baratheon character. It \
should have a name and a boolean indicating if the character is alive."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """This method should initialize the Baratheon character with the \
name and is_alive attributes."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self):
        """This method should return the string representation of the \
Baratheon character."""
        string = f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"
        return string

    def __repr__(self):
        """This method should return the string representation of the \
Baratheon character."""
        return self.__str__()

    def die(self):
        """This method should set the is_alive attribute to False."""
        self.is_alive = False

    @classmethod
    def create_baratheon(cls, first_name: str, is_alive: bool = True):
        """This method should set the first_name of a Baratheon to the given\
 value."""
        return cls(first_name, is_alive)


class Lannister(Character):
    __doc__ = """This children class represents the Lannister character. It \
should have a name and a boolean indicating if the character is alive."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """This method should initialize the Lannister character with the \
name and is_alive attributes."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = 'blue'
        self.hairs = 'light'

    def die(self):
        """This method should set the is_alive attribute to False."""
        self.is_alive = False

    def __str__(self):
        """This method should return the string representation of the \
Lannister character."""
        string = f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"
        return string

    def __repr__(self):
        """This method should return the string representation of the \
Lannister character."""
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """This method should set the first_name of a Lannister to the given\
 value."""
        return cls(first_name, is_alive)
