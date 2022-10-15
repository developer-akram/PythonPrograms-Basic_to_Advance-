# 6. Write a  program to find minimum between three numbers.

num_1 = int(input("Enter 1st number : "))
num_2 = int(input("Enter 2nd number : "))
num_3 = int(input("Enter 3rd number : "))

if num_1 < num_2 and num_1 < num_3 :
    print("1st number = {0} is the minimum number".format(num_1))
if num_2 < num_1 and num_2 < num_3 :
    print("2nd number = {0} is the minimum number".format(num_2))
if num_3 < num_1 and num_3 < num_2 :
    print("3rd number = {0} is the minimum number".format(num_3))
