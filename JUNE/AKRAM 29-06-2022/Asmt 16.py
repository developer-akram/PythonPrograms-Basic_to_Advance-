# 16. Write a   program to calculate sum of digits of a number.

num = int(input("Enter a number : "))
sum = 0
while num > 0 :
    i = num % 10
    sum += i
    num //= 10
print("Sum of the digits = ",sum)