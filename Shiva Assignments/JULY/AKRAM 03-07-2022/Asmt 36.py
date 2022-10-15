# 36. Write a python program to print the first 10 numbers Fibonacci series
a = 0
b = 1
print("First 10 Fibonacci series : ")
for i in range (10):
        c = a + b
        print(a,end="\t")
        a = b
        b = c
