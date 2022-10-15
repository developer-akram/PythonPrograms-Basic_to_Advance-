# ----------------------------------------ASSIGNMENT 3------------------------------------------
# Write a program to add two numbers without using '+' operator.

num_first = int(input("Enter first number : "))
num_second = int(input("Enter second number : "))

list1 = [num_first,num_second]
print("Answer : {0} + {1} = {2}".format(num_first,num_second,sum(list1)))