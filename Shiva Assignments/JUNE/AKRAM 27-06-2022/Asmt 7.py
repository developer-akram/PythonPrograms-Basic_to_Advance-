# 7. Write a program to check whether a number is negative, positive or zero.

num = int(input("Enter a number : "))

if num > 0 :
    print("{} is a positive number".format(num))
else:
    if num < 0:
        print("{} is a negitive number".format(num))
    else:
        print("the number is zero")