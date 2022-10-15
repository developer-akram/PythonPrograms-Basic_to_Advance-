# 15. Write a program to find the sum of the digits of a number accepted from user

num = int(input("Enter a number : "))
length = 0
a = num
while (num > 0 ):
    num = num // 10
    length += 1
sum = 0
for i in range (length):
    r = a % 10
    sum = sum + r
    a = a // 10
print(sum)