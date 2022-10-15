# 1. WAP to check palindrome in String?

name = input("Enter a name : ")
rev = name[::-1]
if name == rev:
    print(name,"is palingdrome")
else:
    print(name,"is not palindrome")