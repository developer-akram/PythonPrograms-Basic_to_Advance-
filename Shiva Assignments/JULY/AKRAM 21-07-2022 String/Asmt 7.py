# 7.WAP to display a strength of password that password is weak, medium,
# and Strong according to predefined cases?
#
# Strong (at least 3 special char, non-consecutive, not belonging with first name
#     and Lastname, one upper case char and numeric is mandatory, length minimum 6)
# Medium (at least 2 special char, non-consecutive, length minimum 6)
#
# Special Characters(32–47 / 58–64 / 91–96 / 123–127)
# Numbers (48-57)
# Letters(65–90 / 97–122)

f_name = input("Enter first name : ")
l_name = input("Enter last name : ")
pwd = input("Enter a password : ")
s_char = b_char = 0
num = special = 0
for i in pwd :
    if ord(i) >= 65 and ord(i) <= 90:
        b_char += 1
    elif ord(i) >= 97 and ord(i) <= 122:
        s_char += 1
    elif ord(i) >= 48 and ord(i) <= 57:
        num += 1
    elif ord(i) >= 32 and ord(i) <= 47 or ord(i) >= 58 and ord(i) <= 64 or \
            ord(i) >= 91 and ord(i) <= 96 or ord(i) >= 123 and ord(i) <= 127:
        special += 1
if b_char > 0 and special > 2 and s_char >= 0 and num > 0 and \
    f_name not in pwd and l_name not in pwd and len(pwd) > 5:
    print("Strong Password : ['%s']"%pwd)
elif special > 1 and len(pwd) > 5 :
    print("Medium Password : ['%s']"%pwd)
else:
    print("Weak password : ['%s']"%pwd)