# 8. WAP to calculate electricity bill where unit price,
# total consumption will be entered by the user,
# if the bill is <400 then pay only 100 RS and above this 50% amount will be paid.

unit_price = int(input("Enter per unit cost : "))
total_unit = int(input("Enter total no of units : "))
total_bill = unit_price * total_unit
print("Total Bill =",total_bill)
print("Pay only 100 Rs") if total_bill < 400 else print("Pay = %.2f"%(total_bill / 2))
