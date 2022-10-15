# 2.) Write a program to print even numbers and odd numbers separately without using if [use for loop only]

num = int(input("Enter a range : "))
print("Even numbers are : ",end="")
for i in range (2, num+1, 2):
    print(i,end=" ")
print("\nOdd numbers are : ",end="")
for i in range (1, num+1, 2):
    print(i,end=" ")