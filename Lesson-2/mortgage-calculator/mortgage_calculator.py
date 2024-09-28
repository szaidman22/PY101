""" Mortgage Calculator """

import os

# Add arrow prefix
def prompt(message):
    print(f'==> {message}')

#Remove comma from loan amount
def remove_comma(number_string):
    return "".join(number_string.split(","))

#test for invalid loan amount input
def invalid_amount(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

#test for invalid month input
def invalid_month(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

#test for invalid y/n response
def invalid_yn(response):
    return response not in ['y','n']

#get valid yes or no response from user
def get_valid_yn(response):
    while invalid_yn(response):
        prompt("Please enter only 'y' or 'n'.")
        response = input().casefold()
    return response

#test for invalid numeric response to change selection
def invalid_change_option(response):
    return response not in ['1','2','3','4']

#get loan amount
def get_loan_amount():
    prompt("Please Enter Loan Amount:")
    loan_amount = remove_comma(input("$"))

    while invalid_amount(loan_amount) or float(loan_amount) <= 0:
        prompt("please enter valid number")
        loan_amount = remove_comma(input("$"))

    loan_amount = float(loan_amount)
    return loan_amount

#get APR
def get_apr():
    prompt("Please Enter APR (%):")
    apr_input = input().strip('%')

    while invalid_amount(apr_input):
        prompt("Please enter a valid percentage")
        apr_input = input().strip('%')

    apr = float(apr_input) / 100
    return apr

#get loan duration
def get_loan_duration_months():
    prompt("Please enter loan duration (in months, whole numbers only):")
    duration_months = input()

    while invalid_month(duration_months) or int(duration_months) <= 0:
        prompt("Please enter a valid number of months")
        duration_months = input()

    duration_months = int(duration_months)
    return duration_months

#collect all inputs
def initial_collection():
    loan_amount = get_loan_amount()
    apr = get_apr()
    duration_months = get_loan_duration_months()

    return loan_amount, apr, duration_months

#have user check their input
def check_input(loan_amount,apr,duration_months):
    prompt("Here is what you've entered:")
    print(f"Loan Amount: ${loan_amount:,}")
    print(f"APR: {apr * 100}%")
    print(f"Loan Duration: {duration_months} months "
        f"({duration_months // 12} years and {duration_months % 12} months)")
    prompt("Does this look correct? (y/n)")

    correct_info = get_valid_yn(input().casefold())

    return correct_info

#get user validated input to be used for monthly payment calculation
def user_validated_input():
    loan_amount, apr, duration_months = initial_collection()

    correct_info = check_input(loan_amount, apr, duration_months)

    while correct_info == 'n':
        prompt("What would you like to change? (enter number)\n"
                "1) Loan Amount\n"
                "2) APR\n"
                "3) Loan Duration\n"
                "4) Start Over")
        to_change = input()

        while invalid_change_option(to_change):
            prompt("Please enter a valid numeric selection:")
            to_change = input()

        match to_change:
            case '1':
                loan_amount = get_loan_amount()
            case '2':
                apr = get_apr()
            case '3':
                duration_months = get_loan_duration_months()
            case '4':
                loan_amount, apr, duration_months = initial_collection()

        correct_info = check_input(loan_amount, apr, duration_months)

    return loan_amount, apr, duration_months

#monthly payment calculation
def get_monthly_payment(loan_amount, apr, duration_months):
    if apr == 0:
        return loan_amount / duration_months
    try:
        monthly_payment = loan_amount * ((apr / 12) / (1 - (1 + (apr / 12)) ** (-duration_months)))
    except OverflowError:
        return "Number cannot be calculated."
    return monthly_payment

#monthly payment output
def payment_ouptut(monthly_payment):
    if isinstance(monthly_payment, float):
        prompt(f"Your monthly payment is: ${monthly_payment:,.2f}")
    else:
        prompt(monthly_payment)

#get the ordinal suffix
def number_suffix(number):
    match str(number)[-1]:
        case '1':
            return str(number) + 'st'
        case '2':
            return str(number) + 'nd'
        case '3':
            return str(number) + 'rd'
        case _ :
            return str(number) + 'th'

# main program
def calculator():
    os.system('clear')
    prompt("Welcome to Mortgage Calculator!")
    calculations = 1

    while True:
        prompt(f"Let's begin your {number_suffix(calculations)} calculation:")
        user_loan_amount, user_apr, user_duration_months = user_validated_input()
        user_monthly_payment = get_monthly_payment(user_loan_amount, user_apr, user_duration_months)
        payment_ouptut(user_monthly_payment)

        prompt("Would you like to calculate another payment? (y/n)")
        another_calculation = get_valid_yn(input().casefold())
        os.system('clear')

        if another_calculation == 'n':
            break

        calculations += 1

    prompt(f"Thank you for using Mortgage Calculator! Total calculations made: {calculations}")

calculator()
