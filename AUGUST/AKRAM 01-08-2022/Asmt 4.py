# 4. Write a program to cyclically rotate an array by one

a = input("Enter the numbers like 1 2 3:")
a = a.split(" ")
a = list(map(int,a))
while True:
    print(a,end=" ")
    last = a[-1]
    a.insert(0,last)
    a.pop()
    x = input()
    if x == "s":
        break