from .field import Field


class Phone(Field):
    def __init__(self, value):
        if not self.is_valid(value):
            raise ValueError("Phone number must be 10 digits long.")
        super().__init__(value)

    @staticmethod
    def is_valid(value):
        return value.isdigit() and len(value) == 10
