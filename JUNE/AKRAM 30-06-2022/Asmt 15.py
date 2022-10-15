# 15. Write a  program to print all Perfect numbers between 1 to n.

range = int(input("Enter a range : "))
num = 2
print("Perfect numbers are : ")
while num <= range:
    count = 0
    i = 1
    while i < num :
        if num % i == 0 :
            count += i
        i += 1
    if count == num :
        print(num)
    num += 1
