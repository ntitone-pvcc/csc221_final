from enum import Enum

# A static type that holds the compound rate (times_per_year) and the name of the 
# interest type. 
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

# This type can create a (CompoundInterestType) given a user input of 1, 2, or 3.
# 1 = MONTHLY
# 2 = QUARTERLY
# 3 = YEARLY
class CompoundInterestTypeWrapper:
    compound_interest_type: CompoundInterestType

    def __init__(self, input_string):
        self.compound_interest_type = self._input_value_to_compound_interest_type(input_string)
    
    # 1, 2, and 3 represent the values shown to the user that correspond with the type
    def _input_value_to_compound_interest_type(self, string):
        if string == '1':
            return CompoundInterestType.MONTHLY
        elif string == '2':
            return CompoundInterestType.QUARTERLY
        elif string == '3':
            return CompoundInterestType.ANNUALLY
        raise ValueError(f"Invalid interest type.  There is no interest type associated with the input value: {string}")