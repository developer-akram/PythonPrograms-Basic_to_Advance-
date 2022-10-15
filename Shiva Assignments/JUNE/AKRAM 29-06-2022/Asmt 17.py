# 17. Write a  program to calculate product of digits of a number.

num = int(input("Enter a number : "))
product = 1
while num > 0 :
    i = num % 10
    product *= i
    num //= 10
print("Product of the digit = ",product)