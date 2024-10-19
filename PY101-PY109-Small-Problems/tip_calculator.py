# Create a simple tip calculator. 
# The program should prompt for a bill amount and a tip rate. 
# The program must compute the tip, then print both the tip and 
# the total amount of the bill. You can ignore input validation 
# and assume that the user will enter valid numbers.


def prompt(string):
    return input(f"===> {string}\n")    

bill_amount = float(prompt("Please enter the bill amount:"))

tip_rate = float(prompt("Please enter the tip rate (as a full percentage out of 100):"))

tip = round(bill_amount * (tip_rate/100), 2)

print(f"The tip will be ${tip} and the total bill will be ${round(bill_amount + tip, 2)}")

#from solution
print(f"The tip is ${tip:.2f}")
print(f"The total is ${bill_amount + tip:.2f}")

