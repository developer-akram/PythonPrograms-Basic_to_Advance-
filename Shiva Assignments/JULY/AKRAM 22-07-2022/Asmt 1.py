# 1. WAP to validate the mobile number?

number = input("Enter mobile number : ")
if len(number) == 10 and int(number[0]) >5 and number.isnumeric() == True:
    print(number,"is a valid number")
else:
    print(number,"is invalid number")
