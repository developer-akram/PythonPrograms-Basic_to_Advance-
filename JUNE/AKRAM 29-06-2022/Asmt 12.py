# 12. Write a   program to count number of digits in a number.

num = int(input("Enter a number : "))
i = 0
while num > 0 :
    num //= 10
    i = i+1
print(i,"digit number.")
