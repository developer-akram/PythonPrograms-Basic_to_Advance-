# 14. Write a program to find the factorial of a number.

num = int(input("Enter a number : "))
fact = 1
for i in range (num,1,-1):
    fact = fact * i
    print("{} * ".format(i),end="")
else:
    print("1 =",fact)