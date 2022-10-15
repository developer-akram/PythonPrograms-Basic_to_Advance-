# 4. WAP to extract numeric, alphabets, and special char
# in separate string in any String?
#
# Special Characters(32–47 / 58–64 / 91–96 / 123–127)
# Numbers (48-57)
# Letters(65–90 / 97–122)

name = input("Type anything you want : ")
numbers = []
strings = []
s_chars = []
for i in name :
    if ord(i) >= 65 and ord(i) <= 90 or ord(i) >= 97 and ord(i) <= 122:
        strings.append(i)
    elif ord(i) >= 48 and ord(i) <= 57:
        numbers.append(i)
    elif ord(i) >= 32 and ord(i) <= 47 or ord(i) >= 58 and ord(i) <= 64 or \
            ord(i) >= 91 and ord(i) <= 96 or ord(i) >= 123 and ord(i) <= 127:
        s_chars.append(i)
print("No of characters {} :\n{}".format(len(strings),strings))
print("No of speaial characters {} :\n{}".format(len(s_chars),s_chars))
print("No of Digits {} :\n{}".format(len(numbers),numbers))