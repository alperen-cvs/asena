from enum import IntEnum

class IntEnum(IntEnum):
    @classmethod
    def find_from_number(cls, number):
        return next((value for value in cls if value.value == number), None)