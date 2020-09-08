import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type", help="input type of payment to calculate", choices=["diff", "annuity"])
parser.add_argument("--principal", help="the principal amount", type=int)
parser.add_argument("--payment", help="The payment amount", type=int)
parser.add_argument("--interest", help="The interest amount", type=float)
parser.add_argument("--periods", help="Number of months", type=int)
args = vars()


# def calculate_other_values(parameter):
#     if parameter == 'n':
#         credit_principal = int(input("Enter the credit principal: "))
#         monthly_payment = int(input("Enter the monthly payment: "))
#         credit_interest = float(input("Enter the credit interest: "))
#         calculate_monthly_payments(credit_principal, monthly_payment, credit_interest)
#     elif parameter == 'a':
#         credit_principal = int(input("Enter the credit principal: "))
#         periods = int(input("Enter the number of periods: "))
#         credit_interest = float(input("Enter the credit interest: "))
#         calculate_annuity(credit_principal, periods, credit_interest)
#     elif parameter == 'p':
#         annuity_payment = float(input("Enter the annuity payment: "))
#         periods = int(input("Enter the number of periods: "))
#         credit_interest = float(input("Enter the credit interest: "))
#         calculate_principal(annuity_payment, periods, credit_interest)


def calculate_principal(annuity_payment, periods, credit_interest):
    i = calculate_nominal_rate(credit_interest)
    principal = math.floor(annuity_payment / ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1)))
    print(f"Your credit principal = {principal}!")
    print(f"Overpayment = {periods * annuity_payment - principal}")


def calculate_nominal_rate(credit_interest):
    nominal_interest_rate = (credit_interest / 100) / 12
    return nominal_interest_rate


def calculate_annuity(credit_principal=0, periods=0, credit_interest=0, payment=0):
    if payment == 0:
        nominal_interest_rate = calculate_nominal_rate(credit_interest)
        annuity_payment = credit_principal * ((nominal_interest_rate * math.pow((1 + nominal_interest_rate), periods)) /
                                              (math.pow((1 + nominal_interest_rate), periods) - 1))
        print(f"Your annuity payment = {math.ceil(annuity_payment)}!")
        print(f"Overpayment = {periods * math.ceil(annuity_payment) - credit_principal}")
    elif credit_principal == 0:
        calculate_principal(payment, periods, credit_interest)
    elif periods == 0:
        calculate_monthly_payments(credit_principal, payment, credit_interest)


def calculate_monthly_payments(credit_principal, monthly_payment, credit_interest):
    nominal_interest_rate = calculate_nominal_rate(credit_interest)
    num_of_months = math.log(monthly_payment / (monthly_payment - nominal_interest_rate * credit_principal),
                             1 + nominal_interest_rate)
    num_of_months = math.ceil(num_of_months)
    time = get_time(num_of_months)
    print(f"It will take {time} to repay this credit!")
    print(f"Overpayment = {num_of_months * monthly_payment - credit_principal}")


def get_time(num_of_months):
    years = num_of_months // 12
    num_of_months = num_of_months % 12
    time = ''
    if years > 0:
        time += (str(years) + " years") if years > 1 else (str(years) + ' year')
        if num_of_months:
            time += ' and '
    if num_of_months > 0:
        time += (str(num_of_months) + " months") if num_of_months > 1 else (str(num_of_months) + ' month')
    return time


def get_diff_payments(principal, periods, interest):
    overpayment = 0
    for i in range(periods):
        payment = principal / periods + calculate_nominal_rate(interest) * (principal - (
                principal * (i + 1 - 1)) / periods)
        payment = math.ceil(payment)
        print(f"Month {i + 1}: payment is {payment}")
        overpayment += payment

    print("\nOverpayment = {}".format(overpayment - principal))

if args.interest == None:
    print("Incorrect parameters")
elif args.type == 'diff' and args.payment:
    print("Incorrect parameters")
elif args.type == 'diff':
    if args.principal is None or args.periods is None or args.interest is None:
        print("Incorrect parameters")
    else:
        get_diff_payments(args.principal, args.periods, args.interest)
elif args.type == 'annuity':
    if args.payment is None and args.principal is None and args.periods is None:
        print("Incorrect parameters")
    elif args.payment is None:
        calculate_annuity(args.principal, args.periods, args.interest)
    elif args.principal is None:
        calculate_annuity(payment=args.payment, periods=args.periods, credit_interest=args.interest)
    elif args.periods is None:
        calculate_annuity(credit_principal=args.principal, payment=args.payment, credit_interest=args.interest)

# what_to_calculate = input("What do you want to calculate?\n"
#                           "type 'n' - for number of monthly payments,\n"
#                           "type 'a' for annuity monthly payment amount,\n"
#                           "type 'p' - for credit principal:\n")
#
# calculate_other_values(what_to_calculate)

# write your code here
# if what_to_calculate == 'm':
#     monthly_payment = int(input("Enter the monthly payment: "))
#     months = round(credit_principal / monthly_payment)
#     print("It will take {} {} to repay the credit".format(months, "month" if months == 1 else "months"))
# elif what_to_calculate == 'p':
#     months = int(input("Enter the number of months: "))
#     monthly_payment = credit_principal / months
#     if monthly_payment % 1 != 0:
#         monthly_payment += 1
#     monthly_payment = int(monthly_payment)
#     last_payment = round(credit_principal - (months - 1) * monthly_payment)
#     if credit_principal % monthly_payment == 0:
#         print(f"Your monthly payment = {monthly_payment}")
#     else:
#         print(f"Your monthly payment = {monthly_payment} and the last payment = {last_payment}")
