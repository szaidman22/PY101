'''
Calculator
'''
import json

with open('calculator/calculator-messages.json', 'r') as file:
    message_language = json.load(file)
    file.close()

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

#test for invalid y/n response depending on language
def invalid_response(response, language):
    if language == "English":
        return response not in ['y','n']
    if language == "Spanish":
        return response not in ['s','n']

text = message_language[0]
current_language = "English"

prompt(text["welcome"])

prompt(text["language_change"])
change = input()

while invalid_response(change, current_language):
    prompt(text["language_change"])
    change = input()

if change == 'y':
    prompt(text["language_option"])
    language_number = input()

    while language_number not in ['1','2']:
        prompt(text["language_option"])
        language_number = input()

    match language_number:
        case '1':
            text = message_language[0]
            current_language = "English"
        case '2':
            text = message_language[1]
            current_language = "Spanish"

while True:
    prompt(text["n1"])
    number1 = input()

    while invalid_number(number1):
        prompt(text["valid_number"])
        number1 = input()

    prompt(text["n2"])
    number2 = input()

    while invalid_number(number2):
        prompt(text["valid_number"])
        number2 = input()

    prompt(text["operation"])
    operation = input()

    while operation not in ['1','2','3','4']:
        prompt(text["operation_invalid"])
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
                output = text["zero"]
            else:
                output = number1 / number2

    if isinstance(output,float):
        prompt(f'The result is: {round(output,4)}')
    else:
        prompt(output)

    prompt(text["another"])
    answer = input()

    while invalid_response(answer, current_language):
        prompt(text["valid_another"])
        answer = input()

    if answer == 'n':
        prompt(text["thanks"])
        break
