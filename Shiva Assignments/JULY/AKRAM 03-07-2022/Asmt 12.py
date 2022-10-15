# 12. Write a program to print table of a number accepted from user.

num = int(input("Enter a number : "))
for i in range (1,11):
    print("{} * {} = {}".format(num,i,num * i))