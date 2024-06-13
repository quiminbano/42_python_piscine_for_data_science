from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    __doc__ = """This grandchildren class represents the King character \
(Diamond Class). It should have a name and a boolean indicating if the \
character is alive."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """This constructor should initialize the King character with the \
a first_name, its is_alive status, and the subattributes content in \
Baratheon class and Lannister classes."""
        super().__init__(first_name, is_alive)

    def set_eyes(self, eyes: str):
        """This method should set the eyes attribute to the given eyes."""
        self.eyes = eyes

    def set_hairs(self, hairs: str):
        """This method should set the hairs attribute to the given hairs."""
        self.hairs = hairs

    def get_hairs(self):
        """This method should return the hairs attribute."""
        return self.hairs

    def get_eyes(self):
        """This method should return the eyes attribute."""
        return self.eyes
