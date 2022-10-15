# 13. Write a  program to find first and last digit of a number.

num = int(input("Enter a number : "))
last = num % 10
while num > 0 :
    first = num % 10
    num //= 10
print("First Digit  = ",first)
print("Last Digit = ",last)