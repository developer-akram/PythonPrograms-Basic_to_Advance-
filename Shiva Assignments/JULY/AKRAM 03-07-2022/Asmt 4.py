# 4. WAP to display fibonacci series?

num = int(input("Enter a range to display fibonacci series : "))
a = 0
b = 1
if num <= 0:
    print("Please enter value greater than 0")
elif num == 1:
    print(a)
else:
    for i in range (num):
        c = a + b
        print(a,end="\t")
        a = b
        b = c
