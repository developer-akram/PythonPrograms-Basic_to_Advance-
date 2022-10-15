# 31. Write a python program to read three numbers (a,b,c) and check
# how many numbers between ‘a’ and ‘b’ are divisible by ‘c’

a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))
c = int(input("Enter value of c : "))

if a > b:
    a, b = b, a
for i in range (a,b+1):
    # print(i)
    if i % 3 == 0:
        print(i,end=" ")