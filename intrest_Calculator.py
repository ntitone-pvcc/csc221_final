#def compound_interest()

#This function makes sure the user selects the correct term
def compound_check (compound_pick):
    while True:
        compound_pick = input("please selected at what frequency you would like to compound to be at. \n monthly(1), quarterly(2), or yearly(3). ")
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

#this function will will tae users length and return how long
def invest_length(x):
    #makes sure the user selects the correct choices
    while True:
        x = input("please pick if you would like to invest for month(1), quarter(2), or year(3) ")
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


    while True:
        y = (input(f"please select how many {z} you would like for "))
        try:
           y = int(y)
           break
        except ValueError:
                print("Error: Please enter a valid integer.")
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


print("welcome to our interest calculator the goal of this is to give you a idea of how much interest you will make")

principal = float(input("how much money would you like to add? $")) #Your starting balance
print(f" you have deposited ${principal}")
interest = float(input("what interest rate would you like? %")) #the interest rate you want
print(f"you would like to have a interest rate of %{interest}")
compound = compound_check(True) #Saving our users compound rate from our function 
print(f"you have chosen a {compound} day compound rate")
print(compound)
length = invest_length(True) #saves the length of the investment window in days
print(length)
p = 1 + interest /compound
o = compound * length
final = principal * p ** o
print(round(final, 2))
#test
