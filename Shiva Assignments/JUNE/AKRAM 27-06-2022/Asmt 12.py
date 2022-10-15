# 12. Write a program to input any alphabet and check whether it is vowel or consonant.

alphabet = input("Enter an alphabet : ")
user_input = alphabet.lower()
if user_input == "a" or user_input == "e" or user_input == "i" or user_input == "o" or user_input == "u" :
    print("Given '{0}' alphabet is Vowel.".format(alphabet))
else:
    print("Given '{0}' alphabet is Consonant.".format(alphabet))