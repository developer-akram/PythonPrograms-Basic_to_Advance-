# 27. Write a program to find the sum of following (Accept values of a, r, n from user)
# a + ar + ar2 + ar3 + ………..arn

a = int(input("Enter the value of a : "))
r = int(input("Enter the value of r : "))
n = int(input("Enter the value of n : "))
ans = 0
for i in range (n+1):
    sum = a * (r ** i)
    ans = ans + sum
print("Answer = ",ans)