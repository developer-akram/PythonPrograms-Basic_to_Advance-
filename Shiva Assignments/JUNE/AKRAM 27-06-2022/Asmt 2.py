# 2. Write a program to check the greatest number amoung 3 numbers .

num_first = int(input("Enter 1st number : "))
num_second = int(input("Enter 2nd number : "))
num_third = int(input("Enter 3rd number : "))

if num_first > num_second and num_first > num_third :
    print("1st number ={0} is greater than {1},{2}".format(num_first,num_second,num_third))
if num_second > num_first and num_second > num_third :
    print("2nd number ={0} is greater than {1},{2}".format(num_second,num_first,num_third))
if num_third > num_first and num_third > num_second :
    print("3rd number ={0} is greater than {1},{2}".format(num_third,num_first,num_second))

