# 9. Write a program to check whether a number is even or odd.

num_input = int(input("Enter a no check it is even or odd : "))

if num_input % 2 == 0:
    print("{0} is even number".format(num_input))
else:
    print("{0} is odd number".format(num_input))