# 2. WAP to convert a string from upper case to lower case
# and lower case to upper case?

print(ord("A"))
print(ord("Z"))
print(ord("a"))
print(ord("z"))
output = ""
name = input("Enter a string : ")
for i in name:
    if ord(i) >= 65 and ord(i) <= 90:
        output = output + chr(ord(i)+32)
    elif ord(i) >= 97 and ord(i) <= 122:
        output = output + chr(ord(i)-32)
print("Input : {}\tOutput : {}".format(name,output))