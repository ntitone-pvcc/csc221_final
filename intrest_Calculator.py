# This program is a simple compound interest calculator that will prompt the user for information regarding their investment, calculate the interest accrued over the length of their
# investment, then display their earnings.

# Declare functions
def compound_check (compound_pick):
    """This function takes the input value 'compound pick' from the user, and converts it into an integer value representing the compounding rate in days."""
    while True:
        compound_pick = input("How often would you like the interest to be compounded?\nMonthly(1), Quarterly(2), or Yearly(3) ")
        if (compound_pick == "1" ):
            x = int(compound_pick)
            if (x == 1):
                print("Your interest will be compounded monthly.")
                return 30
        elif (compound_pick == "2"):
            x = int(compound_pick)
            if (x == 2):
                print("Your interest will be compounded quarterly.")
                return 90
        elif (compound_pick ==  "3"):
            x = int(compound_pick)
            if (x == 3):
                print("Your interest will be compounded yearly.")
                return 365
        else:
            print("sorry thats not a valid choice. please selected again")


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
    # amount = principal * (pow((1 + interest / 100), length))
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

print(f"Your principal investment was ${round(principal,2)}")
print(f"You have a interest rate of {interest}%")
print(f"Your interest is being compounded every {compound} day(s)")
print(f"The overall length of your investment is {length} days")
print(f"Your final balance, including both principal and interest, is ${round(final_amount,2)}")