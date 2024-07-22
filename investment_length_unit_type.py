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
    
class InvestmentLengthUnitWrapper:
    investment_length_unit_type: InvestmentLengthUnitType

    def __init__(self, input_string):
        self.investment_length_unit_type = self._input_value_to_investment_length_unit_type(input_string)
    
    def _input_value_to_investment_length_unit_type(self, string):
        if string == '1':
            return InvestmentLengthUnitType.MONTHS
        elif string == '2':
            return InvestmentLengthUnitType.QUARTERS
        elif string == '3':
            return InvestmentLengthUnitType.YEARS
        raise ValueError(f"Invalid input.  There is no length type associated with the input value: {string}")