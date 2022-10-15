# 8. Write a program to check whether a number is divisible by 5 and 11 or not.

num = int(input("Enter a number :"))

if num == 0:
    print("{0} is not divisible by 5 and 11".format(num))
else:
    if num % 5 == 0 and num % 11 == 0:
        print("{0} is divisible by 5 and 11".format(num))
    else :
        print("{0} is not divisible by 5 and 11".format(num))