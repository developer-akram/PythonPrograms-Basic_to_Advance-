#1.Write a program to input a number and write ots absolute value.

user_input = int(input("Enter any number : "))
if user_input > 0 :
    print("{0} is a positive number.".format(user_input))
    print("Absolute value of {} = {}".format(user_input,user_input))
else :
    user_opt = user_input - 2 * (user_input)
    print("{0} is a negitive number.".format(user_input))
    print("Absolute value of {} = {}".format(user_input, user_opt))
