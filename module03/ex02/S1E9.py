from abc import ABC, abstractmethod


class Character(ABC):
    __doc__ = """This parent abstract class represents a character. \
It should have a name and a boolean indicating if the character is alive."""

    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """This constructor should be able to let the children classes \
initialize the character with the name and is_alive attributes."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """This abstract method should set the is_alive attribute to False."""
        pass


class Stark(Character):
    __doc__ = """This children class represents the Stark character. It \
should have a name and a boolean indicating if the character is alive."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """This method should initialize the Stark character with the \
name and is_alive attributes."""
        super().__init__(first_name, is_alive)

    def die(self):
        """This method should set the is_alive attribute to False."""
        self.is_alive = False
