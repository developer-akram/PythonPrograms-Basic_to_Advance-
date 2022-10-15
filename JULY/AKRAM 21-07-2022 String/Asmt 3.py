# 3. WAP to replace the string char from the next consecutive String char
# (if char will be z then replace by a)?

name = input("Enter a name : ")
output = ""
for i in name:
    if ord(i) == 90:
        output = output + chr(ord(i)-25)
    elif ord(i) == 122:
        output = output + chr(ord(i)-25)
    elif ord(i) >= 65 and ord(i) < 90:
        output = output + chr(ord(i)+1)
    elif ord(i) >= 97 and ord(i) < 122:
        output = output + chr(ord(i)+1)
print("Input : {}\tOutput : {}".format(name,output))