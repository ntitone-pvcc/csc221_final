# This program is a simple compound interest calculator that will prompt the user for information regarding their investment, calculate the interest accrued over the length of their
# investment, then display their earnings.

from compound_interest_type import CompoundInterestType, CompoundInterestTypeWrapper
from investment_length_unit_type import InvestmentLengthUnitType, InvestmentLengthUnitWrapper

# This function calculates the interest
def calculateInterest(principle: float, rate: float, compounded_count: int, years: float,):
    a = principle * ((1 + (float(rate)/float(compounded_count))) ** (float(compounded_count)*years))
    return float(round(a,2))

def create_choices_string():
    values = []
    for (index, interestType) in enumerate(CompoundInterestType, start=0):
        values.append(f"{interestType.name} ({index+1})")

    final = ', '.join(values)
    return final
# Checks to see if the user input is valid
def check_user_principle_input(input):
    try:
        value = float(input)
        return value
    except Exception:
        return None
# Checks to see if the user input is a valid amount
def get_user_principle():
    print("What is your initial investment in U.S. dollars?")
    while True:
        principle = input("")
        checked_user_input = check_user_principle_input(input=principle)
        if checked_user_input != None and checked_user_input >=0:
            return checked_user_input
        else:
            print("Please enter a valid U.S. dollar amount for your initial investment")
# Checks to see if interest rate is valid
def check_user_interest_rate(input):
    try:
        value = float(input) / float(100)
        return value
    except Exception:
        return None
# Gets user input for interest rate
def get_user_interest_rate():
    print("What is the interest rate (as a percentage, e.g., 5 for 5%)?")
    while True:
        interestRate = input("")
        checked_user_input = check_user_interest_rate(input=interestRate)
        if checked_user_input != None:
            return checked_user_input
        else:
            print("Please enter a valid interest rate.")
# Gets user's input for the frequency of compounding
def get_user_compound_rate():
    choices = create_choices_string()
    print(F"How often will the interest be compounded?\n{choices}")
    while True:
        compound_rate = input("")
        try:
            checked_user_input = CompoundInterestTypeWrapper(compound_rate)
            return checked_user_input
        except ValueError as e:
            print(e)

def get_user_length_metric():
    values = []
    for (index, unit) in enumerate(InvestmentLengthUnitType, start=0):
        values.append(f"{unit.name} ({index+1})")
    final = ', '.join(values)
    choices = final
    print(F"Over what unit of time would you like to see your investment grow?\n{choices}")

    while True:
        length_metric = input("")
        try:
            checked_user_input = InvestmentLengthUnitWrapper(length_metric)
            return checked_user_input
        except ValueError as e:
            print(e)

# Checks to see if users input length is valid 
def check_user_length_input(unitType: InvestmentLengthUnitType, duration: int):
    try:
        duration = int(duration)
    except ValueError:
        raise ValueError('Duration must be an integer.')
    
    try:
        days = float(unitType.days) #was int1
    except ValueError:
        raise ValueError('Unit type is not an integer')
    
    result = duration * days
    return result
# Gets users choice for investment length
def display_investment_length(unit_type: InvestmentLengthUnitType):
    print(f"How many {unit_type.name} would you like to invest for? ")
    while True:
        length = input("")
        checked_user_input = check_user_length_input(unitType=unit_type, duration=length)
        if checked_user_input != None:
            return checked_user_input
        else:
            print("Please enter a valid U.S. dollar amount for your initial investment")
# Brings everything together and runs the calculator 
def main():
    principle = get_user_principle()
    print(F"Your principal investment is ${round(principle,2)}.")
    interest_rate = get_user_interest_rate()
    print(F"Your interest rate is {round(interest_rate * 100,2) }%.")
    compound_rate = get_user_compound_rate()
    print(F"Your compounding frequency is {compound_rate.compound_interest_type.name}")
    length_metric = get_user_length_metric()
    print(F"You have selected {length_metric.investment_length_unit_type.name}")
    invest_length = display_investment_length(unit_type=length_metric.investment_length_unit_type)
#    print(F"For an investment length of {int(invest_length)} days")
    total_interest = calculateInterest(
        principle=principle, rate=interest_rate, compounded_count=compound_rate.compound_interest_type.times_per_year, years=float(float(invest_length)/float(365))
    )
    print(F"Over an investment length of {int(invest_length)} days your total earnings, including interest, are estimated to be ${total_interest}")
# This is the beginning of the program
#print("Welcome to our compound interest calculator.\n")
print("This compound interest calculator will provide an estimate of the potential earnings on your investment over a specified period based on the initial principal, interest rate, and compounding frequency.\n")
# Calling the program 
main()