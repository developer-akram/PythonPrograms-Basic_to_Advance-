# 11. Write a   program to find sum of all odd numbers between 1 to n.

num = int(input("Enter a range :"))
sum = 0
i = 1
while i <= num :
    sum += i
    print(i,end=" + ")
    i += 2
print("=",sum)