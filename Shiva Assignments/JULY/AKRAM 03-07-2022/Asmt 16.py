# 16. Write a program to check whether a number is prime or not.

num = int(input("Enter a number : "))
for i in range (2,num):
    if num % i == 0:
        print("{} is not a prime number.".format(num))
        break
else:
    print("{} is a prime number.".format(num))
