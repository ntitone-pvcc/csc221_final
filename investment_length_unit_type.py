from enum import Enum

class InvestmentLengthUnitType(Enum):
    MONTHS = ("Months", 30)
    QUARTERS = ("Quarters", 90)
    YEARS = ("Years", 365)

    days: int
    years: float

    def __init__(self, name, number_of_days):
        self._name_ = name
        self.days = number_of_days
        self.years = number_of_days/365

    def __str__(self):
        return self._name_