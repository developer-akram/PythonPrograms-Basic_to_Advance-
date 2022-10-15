# ----------------------------------------ASSIGNMENT 4------------------------------------------
# Write a program to swapping of 3 numbers.

num_1 = int(input("Enter 1st number : "))
num_2 = int(input("Enter 2nd number : "))
num_3 = int(input("Enter 3rd number : "))

var_1,var_2,var_3 = num_1,num_2,num_3
print("Method 1 :")
print("Before swapping \t\t1st no = {0}, 2nd no = {1}, 3rd no = {2}".format(num_1,num_2,num_3))
num_1,num_2,num_3 = num_2,num_3,num_1
print("After swapping  \t\t1st no = {0}, 2nd no = {1}, 3rd no = {2}".format(num_1,num_2,num_3))
print("Method 2 :")
print("Before swapping \t\t1st no = {0}, 2nd no = {1}, 3rd no = {2}".format(var_1,var_2,var_3))
var_1 = var_1 + var_2 + var_3
var_2 = var_1 - (var_2 + var_3)
var_3 = var_1 - (var_2 + var_3)
var_1 = var_1 - (var_2 + var_3)
print("After swapping  \t\t1st no = {0}, 2nd no = {1}, 3rd no = {2}".format(var_1,var_2,var_3))
