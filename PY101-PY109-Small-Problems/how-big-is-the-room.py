# Build a program that asks the user 
# to enter the length and width of a room, 
# in meters, then prints the room's area 
# in both square meters and square feet.

# P:
# A program that takes two arguments as input,
# length (+ numeric) and width (+ numeric) in meters,
# then prints the product of those arguments 
# in meters (unconverted), then the product converted
# to feet.

# E:
# length 2, width 3 = 6 sq meters, 64.5834 sq ft
# length -2, width 3 = error message
# length -2, width -3 = error message
# length 0, width 3 = error message


# D:
# no data structure required for this algorithm beyond float

# A:
# 1. define a function with two inputs
#   - test if input is valid positive nonzero numeric
#   - if not, error message
#   - if so, assign a variable to the product of the two arguments
#   - assign a variable to that variable multipled by 10.7639
#   - print variable 1 followed by variable 2

def room_size(length, width):
    if length <= 0 or width <= 0:
        print("Make sure your measurements are valid.")
    else:
        sqmeter = length * width
        sqft = sqmeter * 10.7639
        print(f"The room is {sqmeter:.2f} square meters and {sqft:.2f} square feet.")

room_size(3,4)
room_size(0,4)
room_size(123.4,4)

# oops, new code based on solution
length = float(input("Enter room length (numbers only):"))
width = float(input("Enter room width (numbers only):"))

sqmeter = length * width
sqft = sqmeter * 10.7639

print(f"The room is {sqmeter:.2f} square meters and {sqft:.2f} square feet.")