#----------------------------------------ASSIGNMENT 8-------------------------------------------
# Write a program to enter two numbers and perform all arithmetic operations.

num_a  = int(input("Enter first number : "))
num_b  = int(input("Enter second number : "))
print("Addition of {0} + {1} = {2}".format(num_a,num_b,num_a+num_b))
print("Substraction of {0} - {1} = {2}".format(num_a,num_b,num_a-num_b))
print("Multiplication of {0} * {1} = {2}".format(num_a,num_b,num_a*num_b))
print("Division of {0} / {1} = {2}".format(num_a,num_b,num_a/num_b))
print("Modulus of {0} % {1} = {2}".format(num_a,num_b,num_a%num_b))
print("Exponentiation of {0} ** {1} = {2}".format(num_a,num_b,num_a**num_b))
print("Floor division of {0} // {1} = {2}".format(num_a,num_b,num_a//num_b))