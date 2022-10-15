# 7. WAP to check that salary is in income tax
# or not display the total amount and the taxable amount

salary = int(input("Enter annual salary : "))
print("Taxable.\nAmount is",salary,"- 500000 =",salary - 500000) if salary > 500000 else print("Not taxable")

