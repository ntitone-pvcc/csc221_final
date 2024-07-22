from enum import Enum

# A static type that holds the compound rate (times_per_year) and the name of the 
# interest type. 
class InvestmentLengthUnitType(Enum):
    MONTHS = ("Months", 30)
    QUARTERS = ("Quarters", 90)
    YEARS = ("Years", 365)

    days: int

    def __init__(self, name, number_of_days):
        self._name_ = name
        self.days = number_of_days

    def __str__(self):
        return self._name_

# This type can create a (InvestmentLengthUnitType) given a user input of 1, 2, or 3.
# 1 = MONTHS
# 2 = QUARTERS
# 3 = YEARS
class InvestmentLengthUnitWrapper:
    investment_length_unit_type: InvestmentLengthUnitType

    def __init__(self, input_string):
        self.investment_length_unit_type = self._input_value_to_investment_length_unit_type(input_string)
    
    # 1, 2, and 3 represent the values shown to the user that correspond with the type
    def _input_value_to_investment_length_unit_type(self, string):
        if string == '1':
            return InvestmentLengthUnitType.MONTHS
        elif string == '2':
            return InvestmentLengthUnitType.QUARTERS
        elif string == '3':
            return InvestmentLengthUnitType.YEARS
        raise ValueError(f"Invalid input.  There is no length type associated with the input value: {string}")