# 14. Write a program to check whether a character is uppercase or lowercase alphabet.

user_input = input("Enter a character :")
if user_input.islower() == True :
    print("Input string is a lowercase alphabet.")
else:
    if user_input.isupper() == True :
        print("Input string is a uppercase alphabet.")
    else:
        print("Please input correctly...")