# Author:Rayon Anglin
# Date:Created:April 8, 2022 
# Course:ITT103 
# Purpose:Pseudocode algorithm to calculate commission for JamEx salespersons based on individual sales amount and class.

# Program:JamEx Limited Salesperson Commission Calculator

print("Welcome to JamEx Limited Salesperson Commission Calculator")

# User input accepted for salesperson Id. An error is displayed if the input is invalid and looped for a valid input. A program terminator is provided as an option.
while True:
    try:
        SalesID=int(input("< Please enter 'Sales ID' to proceed or '0' to exit >"))
    except ValueError:
        print("< Invalid Sales Id >")
        continue
    if SalesID > 0:
        print("< You entered >:",SalesID)
        break
    else:
        print("< Entry has been cancelled. Goodbye! >")
        exit() 
# User input accepted for sales amount. An error is displayed if the input is invalid and looped for a valid input.
while True:
    try:
        SalesAmt=float(input("< Please enter 'Sales amount' >"))
    except ValueError:
        print("< Invalid Sales Amount >")
        continue
    if SalesAmt >= 0:
        print("<You entered >:$",SalesAmt)
        break
    else:
        print("< Kindly re-enter the Sales Amount >")
        break
# User input accepted for Class type. An error is displayed if the input is invalid and looped for a valid input.
while True:
    try: 
        ClassType=int(input("< Please enter class type >"))
    except ValueError:
        print("< Invalid class type >")
        continue     

    if ClassType < 1 or ClassType > 3: 
        print("< Please re-enter class type >")
    else:
        print("Accessing")
        break
# The variable TotalComm is defined as a return function to calculate the commission 
def TotalComm(CommRate):
    return SalesAmt * CommRate   
# The criteria for 'class type 1' commission rate is 6% for $1000 and lower sale, 7% for over $1000 and under $2000, and 10% for $2000 and more sales
while ClassType == 1:
    if SalesAmt <= 1000:
        CommRate = 0.06
        break
    elif SalesAmt > 1000 < 2000:
        CommRate = 0.07
        break
    else:
        SalesAmt >= 2000
        CommRate = 0.1
        break  
# The criteria for 'class type 2' commission rate is 4% under $1000 sale and 6% over $1000 sale
while ClassType == 2:
    if SalesAmt < 1000:
        CommRate = 0.04
        break
    else:
        SalesAmt >= 1000
        CommRate = 0.06
        break
# The criteria for 'class type 3' is a flat commission rate of 4.5% regardless of the amount of sales         
while ClassType == 3:
    CommRate = 0.045
    break
# Salesperson commission rate and commission total displayed for user to see
print("Your commission rate is:",CommRate)
print("Your total commission is: $",TotalComm(CommRate))
# User may choose to enter another salesperson number or exit the program.      
SalesID=int(input("< Please enter 'Sales ID' to proceed or '0' to exit >"))
