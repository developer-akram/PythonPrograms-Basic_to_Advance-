#-------------------------------------------H ASSIGNMENT 8-------------------------------------------
# 5.WAP to calculate square and cube of any entered number?

user_input = int(input("Enter a number to get its's square and cube : "))
input_square = user_input ** 2
input_cube = user_input ** 3
print("Square : {0}^2 = {1}\nCube : {2}^3 = {3}"
      .format(user_input,input_square,user_input,input_cube))