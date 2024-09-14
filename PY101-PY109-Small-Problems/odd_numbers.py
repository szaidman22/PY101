# Print all odd numbers from 1 to 99 inclusive
# with each number on a separate line
# bonus: can you solve the problem by iterating over
# just the odd numbers?

# PEDAC:
# Process the problem:
# Input: iterable (?)
# Output: odd numbers 1-99 each printed on a separate line
# Mental Model (what the problem requires):
#   Get a collection of integers from 1 to 99 inclusive,
#   iterate over the list to determine which are odd, then
#   print each number on a separate line.
# Algorithm: 
# 1. Create a range
# 2. run the range through a for loop
#   - test for oddness with modulo in if statement, and print if True

for integer in range(0,100):
    if integer % 2 != 0:
        print(integer)

#bonus
# changing algorithm to get range with only odd numbers:

for integer in range(1,100,2):
    print(integer)

# Further Exploration
# Consider adding a way for the user 
# to specify the starting and ending 
# values of the odd numbers printed.

def odd_print(start, stop):
    if start % 2 == 0: 
        start = start + 1
    if stop % 2 != 0:
        stop = stop + 1
    for integer in range(int(start),int((stop)),2):
        print(integer)

# test cases
odd_print(1,99)
odd_print(3,7)
odd_print(-4,10)