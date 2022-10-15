# 25. Write a program to input electricity unit charges and
# calculate total electricity bill according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional survice-charge of 20% is added to the bill

unit_no = float(input("Enter the no of unit : "))
if unit_no < 0:
    print("Unit should be greater than 0")
else:
    if unit_no <= 50 :
        unit_cost = unit_no * 0.50
    else:
        if unit_no > 50 and unit_no <= 150 :
            unit_cost = unit_no * 0.75
        else:
            if unit_no > 150 and unit_no <= 250:
                unit_cost = unit_no * 1.20
            else:
                unit_cost = unit_no * 1.50
total_cost = unit_cost + unit_cost * 0.20
print("Total electricity bill = %.2f"%total_cost)