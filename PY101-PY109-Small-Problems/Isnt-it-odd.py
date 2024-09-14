# Write a function that takes one integer argument
# and reutrns True when the number's absolute value
# is odd, False otherwise

#PEDAC:
# Process the Problem:
# Input: integer (positive, negative, 0)
# Output: boolean

def odd_test(integer):
    if not type(integer) == int:
        print("Please enter an integer")
    elif abs(integer) % 2 == 0:
        return False
    else:
        return True

#Examples
odd_test(1) 
odd_test(-3)    
odd_test(0)  
odd_test(900)  
odd_test(-4)
odd_test(-3.6)

#alternate based on solution
def odd_test(integer):
    if not type(integer) == int:
        print("Please enter an integer")
    else:
        return abs(integer) % 2 == 0
        
#Examples
odd_test(1) 
odd_test(-3)    
odd_test(0)  
odd_test(900)  
odd_test(-4)
odd_test(-3.6)