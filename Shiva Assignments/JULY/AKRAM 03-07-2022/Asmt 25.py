# 25. Write a program to accept a number and check whether it is a perfect number or not.

num = int(input("Enter a number : "))
sum= 0
for i in range (1,num):
    if num % i == 0:
        sum = sum + i
if num == sum:
    print(num,"is a Perfect number.")
else:
    print(num,"is not a Perfect number.")
