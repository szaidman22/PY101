'''
Calculator
'''

#add arrow prefix
def prompt(message):
    print(f'==> {message}')

#test for invalid input
def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

prompt("Welcome to Calculator!")

prompt("What's the first number?")
number1 = input()

while invalid_number(number1):
    prompt("Please enter a valid number.")
    number1 = input()

prompt("What's the second number?")
number2 = input()

while invalid_number(number2):
    prompt("Please enter a valid number.")
    number2 = input()

prompt("What operation would you like to perform? (enter number):\n"
      "1) Add\n"
      "2) Subtract\n"
      "3) Multiply\n"
      "4) Divide")
operation = input()

#test for in
# valid operation number
while operation not in ['1','2','3','4']:
    prompt("Oops, please enter a valid operation number:\n"
           "1) Add\n"
           "2) Subtract\n"
           "3) Multiply\n"
           "4) Divide")
    operation = input()

number1 = float(number1)
number2 = float(number2)

match operation:
    case '1':
        output = number1 + number2
    case '2':
        output = number1 - number2
    case '3':
        output = number1 * number2
    case '4':
        if number2 == 0:
            output = "Dividing by 0 is not allowed!"
        else:
            output = number1 / number2
    case _:
        output = "Something went awry!"

if isinstance(output,float):
    prompt(f'The result is: {round(output,4)}')
else:
    prompt(output)
