# Ask user for first number
# Ask user for second number
# Ask use for operation to perform
# perform operation on two numbers
# print the result to the terminal

print("Welcome to Calculator!")

print("What's the first number?")
number1 = float(input())
print("What's the second number?")
number2 = float(input())

print("What operation would you like to perform? (enter number):\n"
      "1) Add\n"
      "2) Subtract\n"
      "3) Multiply\n"
      "4) Divide")
operation = input()

if operation == '1':
    output = number1 + number2
elif operation == '2':
    output = number1 - number2
elif operation == '3':
    output = number1 * number2
elif operation == '4':
    if number2 == 0:
        output = "Dividing by 0 is not allowed!"
    else:
        output = number1 / number2
else:
    output = "Oopsie, please select a valid operation."

if type(output) == float:
    print(f'The result is: {round(output,4)}')
else:
    print(output)