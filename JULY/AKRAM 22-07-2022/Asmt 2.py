# 2. WAP to validate first name and last name?
f_name = input("Enter first name : ")
l_name = input("Enter last name : ")
print("Hint! username is your firstname and password is lastname")
user = input("Enter username : ")
pwd = input("Enter password : ")
if f_name == user and l_name == pwd:
    print("Login successfully....")
elif f_name == user and l_name != pwd:
    print("Invalid password")
elif f_name != user and l_name == pwd:
    print("Invalid username")
else:
    print("Invalid username and password")