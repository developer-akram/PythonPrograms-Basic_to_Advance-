# 35. Write a python program to print the factorial of a given number

num = int(input("Enter a number : "))
fact = 1
for i in range (num,1,-1):
    fact = fact * i
    print("{} * ".format(i),end="")
else:
    print("1 =",fact)