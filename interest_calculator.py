# This program is a simple compound interest calculator that will prompt the user for information regarding their investment, calculate the interest accrued over the length of their
# investment, then display their earnings.

from compound_interest_type import CompoundInterestType, CompoundInterestTypeWrapper
from investment_length_unit_type import InvestmentLengthUnitType, InvestmentLengthUnitWrapper

def calculateInterest(principle: float, rate: float, compounded_count: int, years: float,):
    a = principle * ((1 + (float(rate)/float(compounded_count))) ** (float(compounded_count)*years))
    return float(round(a,2))

def create_choices_string():
    values = []
    for (index, interestType) in enumerate(CompoundInterestType, start=0):
        values.append(f"{interestType.name} ({index+1})")

    final = ', '.join(values)
    return final

def check_user_principle_input(input):
    try:
        value = float(input)
        return value
    except Exception:
        return None

def get_user_principle():
    print("What is your initial investment in U.S. dollars?")
    while True:
        principle = input("")
        checked_user_input = check_user_principle_input(input=principle)
        if checked_user_input != None:
            return checked_user_input
        else:
            print("Please enter a valid U.S. dollar amount for your starting investment")

def check_user_interest_rate(input):
    try:
        value = float(input) / float(100)
        return value
    except Exception:
        return None

def get_user_interest_rate():
    print("What is the interest rate of your investment?")
    while True:
        interestRate = input("")
        checked_user_input = check_user_interest_rate(input=interestRate)
        if checked_user_input != None:
            return checked_user_input
        else:
            print("Please enter a valid interest rate.")

def get_user_compound_rate():
    choices = create_choices_string()
    print(F"How often should your interest compound?\n{choices}")
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
    print(F"What unit of time would you like to see your investment grow in?\n{choices}")

    while True:
        length_metric = input("")
        try:
            checked_user_input = InvestmentLengthUnitWrapper(length_metric)
            return checked_user_input
        except ValueError as e:
            print(e)


def check_user_length_input(unitType: InvestmentLengthUnitType, duration: int):
    try:
        duration = int(duration)
    except ValueError:
        raise ValueError('Duration must be an integer.')
    
    try:
        days = int(unitType.days)
    except ValueError:
        raise ValueError('Unit type is not an integer')
    
    result = duration * days
    return result

def display_investment_length(unit_type: InvestmentLengthUnitType):
    print(f"How many {unit_type.name} would you you like to invest for? ")
    while True:
        length = input("")
        checked_user_input = check_user_length_input(unitType=unit_type, duration=length)
        if checked_user_input != None:
            return checked_user_input
        else:
            print("Please enter a valid U.S. dollar amount for your starting investment")
    
def main():
    principle = get_user_principle()
    print(F"Your principle is ${principle}.")
    interest_rate = get_user_interest_rate()
    print(F"Your interestRate is {interest_rate * 100 }%.")
    compound_rate = get_user_compound_rate()
    print(F"Your compound rate is {compound_rate.compound_interest_type.name}")
    length_metric = get_user_length_metric()
    print(F"You have selected {length_metric.investment_length_unit_type.name}")
    invest_length = display_investment_length(unit_type=length_metric.investment_length_unit_type)
    print(F"Your investment length is over {invest_length} days")
    total_interest = calculateInterest(
        principle=principle, rate=interest_rate, compounded_count=compound_rate.compound_interest_type.times_per_year, years=float(float(invest_length)/float(365))
    )
    print(F"Your total interest is {total_interest}")


main()