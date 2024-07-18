#This function makes sure the user selects the correct compound rate that they want the compound rate to be 
def compound_check (compound_pick):
    while True:
        compound_pick = input("please selected at what frequency you would like to compound to be at. \nmonthly(1), quarterly(2), or yearly(3). ")
        if (compound_pick == "1" ):
            x = int(compound_pick)
            if (x == 1):
                print("you have chosen monthly")
                return 30
        elif (compound_pick == "2"):
            x = int(compound_pick)
            if (x == 2):
                print("You have chosen quarterly")
                return 90
        elif (compound_pick ==  "3"):
            x = int(compound_pick)
            if (x == 3):
                print("you have chosen yearly")
                return 365
        else:
            print("sorry thats not a valid choice. please selected again")

#this function will take users input and return how long in days
def invest_length(x):
    #makes sure the user selects the correct choices so that it can be assigned to z 
    while True:
        x = input("would you like your investment length to be in \nmonth(1), quarter(2), or year(3) ")
        if (x == "1"):
            x = int(x)
            if (x == 1):
                z = "month"
                break
        elif (x == "2"): 
            x = int(x)
            if (x == 2):
                z = "quarter"
                break
        elif (x == "3"):
            x = int(x)
            if (x == 3):
                z = "year"
                break
        else:
            print("sorry please select again from the choices listed")

    #checks to see if the user entered a string that can be converted to a int
    while True:
        y = (input(f"please select how many {z} you would like for "))
        try:
           y = int(y)
           break
        except ValueError:
                print("Error: Please enter a valid integer.")

    #Multiples days by the duration you have picked to give total number of days you are investing for            
    while True:     
        if (x == 1):
            print("You have selected month")
            return 30 * y
        elif (x == 2):
            print("You have selected quarter")
            return 90 * y
        elif (x == 3):
            print("You have selected year")
            return 365 * y
        else:
            print("sorry thats not a valid choice. Please select again")

#Does all the math
def compound_interest(principal, interest, length, compound):
    # Calculate compound interest
    #amount = principal * (pow((1 + interest / 100), length))
    amount = principal * (pow((1 + interest / (100 * compound)), compound * length))
    total = amount - principal
    return total


print("welcome to our interest calculator the goal of this is to give you a idea of how much interest you will make")
#saving variables 
principal = float(input("how much money would you like to add? $")) #Your starting balance
print(f" you have chosen deposited ${principal}")
interest = float(input("what interest rate would you like? %")) #the interest rate you want
print(f"you have chosen to have a interest rate of %{interest}")
compound = compound_check(True) #Saving our users compound rate from our function 
print(f"you have chosen a {compound} day compound rate")
length = invest_length(True) #saves the length of the investment window in days
final_amount = compound_interest(principal, interest, length, compound)

print(f"your starting amount is ${principal}")
print(f"you have a interest rate of %{interest}")
print(f"you have selected your term to be for {length} days")
print(f"with it compounding every {compound} days")
print(f"your final amount after everything should be ${final_amount}")

      #math part
#p = 1 + interest /compound
#o = compound * length
#final = principal * p ** o
#print(round(final, 2))

