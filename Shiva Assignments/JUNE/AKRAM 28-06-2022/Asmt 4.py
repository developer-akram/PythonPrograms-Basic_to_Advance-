# 4. Write a program to check the input number is one digit positive or negitive

num = int(input("Enter a number : "))

if num >= -9 and num <= 9 :
    if num < 0 :
        print("One digit negitive number.")
    elif num == 0 :
        print("Number is zero.")
    else :
        print("One digit positive number.")
else:
    print("Invalid input.Please try again...")