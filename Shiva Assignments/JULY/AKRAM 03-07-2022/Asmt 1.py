# 1. Write a program to print number 1 to n using for loop
print("Program of 1 to n")
num = int(input("Enter a range : "))
for i in range (1, num+1):
    print(i,end=" ")

#2. Write a program to print number n to 1 using for loop

print("\nProgram of n to 1")
num = int(input("Enter a range to print in reverse order : "))
for i in range (num, 0, -1):
    print(i,end=" ")
