# ----------------------------------------------H ASSIGNMENT 6----------------------------------------------
# WAP to reverse the five-digit number where the first and last digit will be in the same position.

user_input = int(input("Enter a 5 digit number : "))
a1 = user_input % 10
b1 = user_input // 10
a2 = b1 % 10
b2 = b1 // 10
a3 = b2 % 10
b3 = b2 // 10
a4 = b3 % 10
b4 = b3 // 10

user_output = b4*10000 + a2*1000 + a3*100 + a4*10 + a1
print("The output is = ",user_output)