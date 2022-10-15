# 9. WAP  TO CHECK THAT USERNAME AND PASSWORD BOTH ARE CORRECT OR NOT WHERE
# USERNAME IS YOUR FIRST NAME AND PASSWORD YOUR LASTNAME?
# PROVIDE SEPARATE MESSAGES FOR INVALID USERNAME, INVALID PASSWORD, INVALID USERNAME, AND PASSWORD?

name_f = input("Enter your first name : ")
name_l = input("Enter your last name : ")
print("Your First name = username and last name = password")
username = input("Enter username : ")
password  = input("Enter password : ")
if name_f == username and name_l == password :
    print("Login Sucessfully")
elif name_f != username and name_l != password :
    print("Invalid username and password")
elif name_f != username :
    print("Invalid username")
elif name_l != password :
    print("Invalid password")