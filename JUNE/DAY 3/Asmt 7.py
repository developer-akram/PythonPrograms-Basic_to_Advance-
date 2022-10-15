#----------------------------------------ASSIGNMENT 7--------------------------------------------
# Q. If a four-digit number is input through the keyboard, write a
# program to obtain the sum of the first and last digit of this number.

user_input = int(input("Enter any four digit number : "))
a1 = user_input % 10
b1 = user_input // 10
a2 = b1 % 10
b2 = b1 // 10
a3 = b2 % 10
b3 = b2 // 10

user_output_sum = b3 + a1
print("Sum of first and last digit of the number {0} = {1} + {2} = {3}"
      .format(user_input,b3,a1,user_output_sum))
