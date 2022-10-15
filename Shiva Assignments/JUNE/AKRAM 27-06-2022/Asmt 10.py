# 10. Write a program to check whether a year is leap year or not.

year_input = int(input("Enter a year to check leap year or not :"))

if year_input % 400 == 0:
    print("{0} is a leap year".format(year_input))
else:
    if year_input % 4 == 0 and year_input % 100 != 0:
        print("{0} is a leap year".format(year_input))
    else:
        print("{0} is not a leap year".format(year_input))