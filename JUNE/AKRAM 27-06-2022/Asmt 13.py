# 13. Write a program to input any character and check whether it is alphabet, digit or special character.

list1 = ["@","_","!","#","$","%","^","&","*","(",")","<",">","?","/","|","{","}","~",":","[","]"]

user_input = input("Enter any :")
if user_input in list1:
    print("'{0}' is a Special Character.".format(user_input))
else:
    if user_input.isalpha() == True:
        print("'{0}' is an Alphabet.".format(user_input))
    else:
        print("'{0}' is a Digit.".format(user_input))