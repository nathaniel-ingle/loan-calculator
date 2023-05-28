import argparse
from math import ceil, log

parser = argparse.ArgumentParser()
parser.add_argument("--type",
                    choices=["diff", "annuity"])
parser.add_argument("--principal")
parser.add_argument("--payment")
parser.add_argument("--periods")
parser.add_argument("--interest")
args = parser.parse_args()

calc_type = args.type
try:
    principal = int(args.principal)
except:
    principal = args.principal
try:
    payment = int(args.payment)
except:
    payment = args.payment
try:
    periods = int(args.periods)
except:
    periods = args.periods
try:
    interest = float(args.interest)
except:
    interest = args.interest


def calc_annuity(principal, number_of_payments, interest):
    nominal_interest = interest / 1200
    numerator = nominal_interest * (1 + nominal_interest) ** number_of_payments
    denominator = ((1 + nominal_interest) ** number_of_payments) - 1
    monthly_annuity = ceil(principal * (numerator / denominator))
    total_interest = (monthly_annuity * number_of_payments) - principal
    print("Your monthly payment = ", monthly_annuity, "!", sep="")
    print("Overpayment =", total_interest)


def calc_principal(annuity, number_of_payments, interest):
    nominal_interest = interest / 1200
    numerator = nominal_interest * (1 + nominal_interest) ** number_of_payments
    denominator = (1 + nominal_interest) ** number_of_payments - 1
    principal_amount = annuity / (numerator / denominator)
    print("Your loan principal = ", int(principal_amount), "!", sep="")
    print("Overpayment =", ceil((annuity * number_of_payments) - principal_amount))


def calc_payments(principal, annuity, interest):
    nominal_interest = interest / 1200
    x = (annuity / (annuity - nominal_interest * principal))
    number_of_payments = ceil(log(x, (1 + nominal_interest)))
    payment_years = number_of_payments // 12
    payment_months = number_of_payments % 12
    if payment_years == 0:
        print("It will take", payment_months, "months to repay this loan!")
    elif payment_months == 0:
        print("It will take", payment_years, "years to repay this loan!")
    else:
        print("It will take", payment_years, "years and", payment_months, "months to repay this loan!")
    print("Overpayment = ", (annuity * number_of_payments) - principal)


def differentiate(principal, periods, interest):
    nominal_interest = interest / 1200
    final_payment = 0
    for i in range(periods):
        month_payment = ceil((principal / periods) + nominal_interest * (principal - ((principal * i) / periods)))
        final_payment += month_payment
        print("Month ", i + 1, ": payment is ", month_payment, sep="")
    print()
    print("Overpayment =", final_payment - principal)



def valid_parameters(parameters):
    return None not in parameters and not any(map(lambda n: n < 0, parameters))


if calc_type == "diff" and valid_parameters([principal, periods, interest]):
    differentiate(principal, periods, interest)
elif calc_type == "annuity":
    if valid_parameters([principal, periods, interest]):
        calc_annuity(principal, periods, interest)
    elif valid_parameters([payment, periods, interest]):
        calc_principal(payment, periods, interest)
    elif valid_parameters([principal, payment, interest]):
        calc_payments(principal, payment, interest)
    else:
        print("Incorrect parameters.")

else:
    print("Incorrect parameters.")
