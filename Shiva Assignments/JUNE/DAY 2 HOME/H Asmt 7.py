#-------------------------------------H ASSIGNMENT 7----------------------------------------
# 4.WAP to swap two numbers without using a third variable

num_first = int(input("Enter first number : "))
num_second = int(input("Enter second number : "))
print("Before Swapping\t\t1st number = {0} || 2nd number = {1}".format(num_first,num_second))
num_first = num_first + num_second
num_second = num_first - num_second
num_first = num_first - num_second
print("After Swapping \t\t1st number = {0} || 2nd number = {1}".format(num_first,num_second))