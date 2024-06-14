import random
import string
from dataclasses import dataclass, field


def class_check(func):

    def wrapper(*args, **kwargs):
        try:
            func_output = func(*args, **kwargs)
            return func_output
        except Exception as e:
            print(f"{e.__class__.__name__}: {e}")
            return None
    return wrapper


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@class_check
@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        assert isinstance(self.name, str), "name is not a string"
        assert isinstance(self.surname, str), "surname is not a string"
        assert isinstance(self.active, bool), "active is not a boolean"
        assert self.name, "name is empty"
        assert self.surname, "surname is empty"
        self.login = self.name[0] + self.surname
