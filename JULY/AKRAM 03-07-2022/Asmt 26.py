# 26. Write a program to find the sum of the following series(accept values of x and n from user)
# 1 + x/1! + x2/2! + ……….xn/n!

x = int(input("Enter the value of x : "))
n = int(input("Enter the value of n : "))
value = 1
for i in range (1,n+1):
    fact = 1
    for j in range (1,i+1):
        fact = fact * j
    value = value + (x**i)/fact
print("Answer = %.2f"%value)
