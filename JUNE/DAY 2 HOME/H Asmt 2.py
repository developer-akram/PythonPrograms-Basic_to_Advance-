# -----------------------------------------------H ASSIGNMENT 2---------------------------------------------------
# 2)  WAP to calculate electricity bill where unit price, total consumption, the extra load will be entered by the users?

unit_price = int(input("Enter the Electricity bill cost per unit : "))
unit_consume = float(input("Enter total consumption unit : "))
extra_load = int(input("Enter the extra load [per 1kW penalty 100/-] : "))

total_bill = (unit_price * unit_consume) + (100 * extra_load)

print("Total elctricity Bill amount = {0}/-".format(total_bill))
