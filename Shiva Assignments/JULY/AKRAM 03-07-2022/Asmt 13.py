# 13. Write a program to display product of the digits of a number accepted from the user.

num = int(input("Enter a number : "))
print("Factors of {} = ".format(num),end="")
for i in range (1,num+1):
    if num % i == 0:
        print(i,end=" ")
