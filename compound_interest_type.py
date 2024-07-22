from enum import Enum


class CompoundInterestType(Enum):
    MONTHLY = ("Monthly", 12)
    QUARTERLY = ("Quarterly", 4)
    ANNUALLY = ("Annually", 1)

    times_per_year: int

    def __init__(self, name, times_per_year):
        self._name_ = name
        self.times_per_year = times_per_year

    def __str__(self):
        return self._name_