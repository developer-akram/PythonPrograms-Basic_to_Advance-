# 4.WAP to check leap year using a ternary operator in Python?

year = int(input("Enter year : "))

x = "Leap year" if year % 400 == 0 else "Leap year" if year % 4 == 0 and year % 100 !=0 else "Not a leap year"
print(x)