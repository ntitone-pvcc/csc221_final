# This program is a simple compound interest calculator that will prompt the user for information regarding their investment, calculate the interest accrued over the length of their
# investment, then display their earnings.

from compound_interest_type import CompoundInterestType
from investment_length_unit_type import InvestmentLengthUnitType

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
        

class CompoundInterestTypeWrapper:
    compound_interest_type: CompoundInterestType

    def __init__(self, input_string):
        self.compound_interest_type = self._input_value_to_compound_interest_type(input_string)
    
    def _input_value_to_compound_interest_type(self, string):
        if string == '1':
            return CompoundInterestType.MONTHLY
        elif string == '2':
            return CompoundInterestType.QUARTERLY
        elif string == '3':
            return CompoundInterestType.ANNUALLY
        raise ValueError(f"Invalid interest type.  There is no interest type associated with the input value: {string}")


def calculateInterest(principle: float, rate: float, compounded_count: int, years: float,):
    a = principle * ((1 + (float(rate)/float(compounded_count))) ** (float(compounded_count)*years))
    return float(round(a,2))

a = calculateInterest(
    principle=100,
    rate=5/100,
    compounded_count=12,
    years=1
)

print(a)

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


# Declare functions
def compound_check (compound_pick):
    # This function takes the input value 'compound pick' from the user, and converts it into an integer value representing the compounding rate in days.
    while True:
        compound_pick = input("How often would you like the interest to be compounded?\nMonthly(1), Quarterly(2), or Yearly(3) ")
        if (compound_pick == "1" ):
            x = int(compound_pick)
            if (x == 1):
                print("Your interest will be compounded monthly.")
                return 12
        elif (compound_pick == "2"):
            x = int(compound_pick)
            if (x == 2):
                print("Your interest will be compounded quarterly.")
                return 4
        elif (compound_pick ==  "3"):
            x = int(compound_pick)
            if (x == 3):
                print("Your interest will be compounded yearly.")
                return 1
        else:
            print("Sorry thats not a valid choice. Please selected again.")


def invest_length(x):
    """This function prompts the user for an investment length in increments of 'x', then converts it into a number of days for further processing."""
    # Forces the user to make a numerical choice, an integer between 1 and 3, which is then assigned to z. 
    while True:
        x = input("Would you like your investment length to be calculated over\nMonths(1), Quarters(2), or Years(3) ")
        if (x == "1"):
            x = int(x)
            if (x == 1):
                z = "months"
                break
        elif (x == "2"): 
            x = int(x)
            if (x == 2):
                z = "quarters"
                break
        elif (x == "3"):
            x = int(x)
            if (x == 3):
                z = "years"
                break
        else:
            print("sorry please select again from the choices listed")

    # Checks to see if the user entered a string that can be converted to an integer
    while True:
        y = (input(f"What is the total length of your investment in {z}. "))
        try:
           y = int(y)
           break
        except ValueError:
                print("Error: Please enter a valid integer.")

    # Multiplies days by the duration you have picked to give total number of days you are investing for            
    while True:     
        if (x == 1):
            #print("You have selected months")
            return 30 * y
        elif (x == 2):
            #print("You have selected quarters")
            return 90 * y
        elif (x == 3):
            #print("You have selected years")
            return 365 * y
        else:
            print("sorry thats not a valid choice. Please select again")

def compound_interest(principal, interest, length, compound):
    """Uses 'principal', 'interest', 'length' and 'compound', to perform a calculation based on the compound interest formula 'A = P(1+r/n)**(n*t)'"""
    # Calculate compound interest
    amount = principal * (pow((1 + interest / (100 * compound)), compound * (length / 365)))
    total = amount - principal
    return total

# Begin our program

# Introduce the program to the user.
print("Welcome to our compound interest calculator. This program will ask you for some basic information regarding your investment, and then caclulate how much interest you will earn over  a given time.")

# Get input from the user
while True:
    p = input("What is your initial investment? $") # Starting balance (principal).
    try:
       p = float(p)
       break
    except ValueError:
            print("Error: Please enter a valid amount.")
while True:
    i = input("What is the interest rate (as a percentage, e.g., 5 for 5%)? ") # The interest rate
    try:
        i = float(i)
        break
    except ValueError:
        print("Please enter a valid interest rate")

# Assign values to variables 
principal = p
#print(f"Your initial investment was for ${principal}")
interest = i
#print(f"you have chosen to have a interest rate of {interest}%")
compound = compound_check(True) #Saving our users compound rate from our function 
#print(f"you have chosen a {compound} day compound rate")
length = invest_length(True) #saves the length of the investment window in days
total_interest = compound_interest(principal, interest, length, compound)
final_amount = total_interest + principal

print(f"Your principal investment was ${principal}")
print(f"You have a interest rate of {interest}%")
print(f"Your interest is being compounded every {compound} day(s)")
print(f"The overall length of your investment is {length} days")
print(f"Your final balance, including both principal and interest, is ${final_amount}")