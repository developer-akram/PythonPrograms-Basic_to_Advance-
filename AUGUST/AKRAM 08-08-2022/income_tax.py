income = int(input("Enter annual income : "))
l2 = 250000
l5 = 500000
l7 = 750000
l10 = 1000000
l12 = 1250000
l15 = 1500000

if income > 0 and income < l2:
    print("Income not in tax criteria.")
elif income < l5:
    tax = (income - l2) * 0.05
    print("Tax amount of {} = {}".format(income,tax))
elif income < l7:
    tax = 12500 + (income - l5) * 0.10
    print("Tax amount of {} = {}".format(income,tax))
elif income < l10:
    tax = 37500 + (income - l7) * 0.15
    print("Tax amount of {} = {}".format(income,tax))
elif income < l12:
    tax = 75000 + (income - l10) * 0.20
    print("Tax amount of {} = {}".format(income,tax))
elif income < l15:
    tax = 125000 + (income - l12) * 0.25
    print("Tax amount of {} = {}".format(income,tax))
else:
    tax = 187500 + (income - l15) * 0.30
    print("Tax amount of {} = {}".format(income,tax))