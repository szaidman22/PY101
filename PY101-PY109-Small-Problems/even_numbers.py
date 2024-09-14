# Print all even numbers from 1 to 99 inclusive
# with each number on a separate line
# bonus: can you solve the problem by iterating over
# just the even numbers?

# PEDAC:
# Process the problem:
# Input: iterable (?)
# Output: even numbers 1-99 each printed on a separate line
# Mental Model (what the problem requires):
#   Get a collection of integers from 1 to 99 inclusive,
#   iterate over the list to determine which are odd, then
#   print each number on a separate line.
# Algorithm: 
# 1. Create a range
# 2. run the range through a for loop
#   - test for evenness with modulo in if statement, and print if True

for integer in range(0,100):
    if integer < 1:
        continue
    if integer % 2 == 0:
        print(integer)

#bonus
# changing algorithm to get range with only even numbers:

for integer in range(2,100,2):
    print(integer)
