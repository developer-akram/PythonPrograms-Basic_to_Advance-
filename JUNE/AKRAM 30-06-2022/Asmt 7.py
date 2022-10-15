# 7. Write a   program to enter a number and print its reverse.

num = int(input("Enter any number : "))
sum = 0
while num > 0 and num !=0 :
    reminder = num % 10
    sum = sum * 10 + reminder
    num //= 10
print("Reverse =",sum)