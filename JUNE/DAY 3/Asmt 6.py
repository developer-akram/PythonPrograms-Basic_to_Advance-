# -----------------------------------------ASSIGNMENT 6-----------------------------------
# Q. If a five-digit number is input through the keyboard, write a
# program to calculate the sum of its digits.

user_input = int(input("Enter a five digit number : "))
a1 = user_input % 10
b1 = user_input // 10
a2 = b1 % 10
b2 = b1 // 10
a3 = b2 % 10
b3 = b2 // 10
a4 = b3 % 10
b4 = b3 // 10
sum_input = a1 + a2 +a3 +a4 + b4
print("Sum of {0} = {1}+{2}+{3}+{4}+{5} = {6}".format(user_input,b4,a4,a3,a2,a1,sum_input))
