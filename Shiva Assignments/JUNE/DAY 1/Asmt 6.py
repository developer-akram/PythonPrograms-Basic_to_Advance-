#--------------------------------------ASSIGNMENT 6-----------------------------------------
# Two numbers are input through the keyboard into two locations C and D.
# Write a program to interchange the contents of C and D.

num_first = int(input("Enter first Number : "))
num_second = int(input("Enter second Number : "))
print("Before swapping First number  = ",num_first)
print("Before swapping Second number  = ",num_second)

num_first = num_first + num_second
num_second = num_first - num_second
num_first = num_first - num_second

print("After swapping First number  = ",num_first)
print("After swapping Second number  = ",num_second)

