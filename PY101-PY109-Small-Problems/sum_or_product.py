# Write a program that asks the user to 
# enter an integer greater than 0, then 
# asks whether the user wants to determine 
# the sum or the product of all numbers between 
# 1 and the entered integer, inclusive.

def bad_sum_product_input(string):
    if len(string) < 1:
        return True
    return string[0].casefold() not in ('s', 'p')

def sum_calc(range):
    sum = 0
    for n in range:
        sum += n
    return sum

def product_calc(range):
    product = 1
    for n in range:
        product *= n
    return product

integer_input = int(input("Enter an integer greater than 0: "))

sum_or_product = input("Do you want to calculate the sum or the product"
                       f"of all numberse between 1 and {integer_input} inclusive?\n"
                       "Enter ""S"" for sum or ""P"" for product.\n")

while bad_sum_product_input(sum_or_product):
    sum_or_product = input("Please enter either ""S"" for sum or ""P"" for product.\n")

choice = sum_or_product.casefold() 

calculation_range = range(1, (integer_input + 1))

match choice:
    case 's':
        calc_output = sum_calc(calculation_range)
    case 'p':
        calc_output = product_calc(calculation_range)
    case _ :
        calc_output = 0


if calc_output > 1000000:
    print(f"{calc_output:,.3e}")
else:
    print(f"{calc_output:,}")
