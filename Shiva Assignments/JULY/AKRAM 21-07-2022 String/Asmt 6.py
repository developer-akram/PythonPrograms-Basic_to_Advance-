# 6. WAP to validate emaild?
# (@, ., the position of @ should be lesser of last dot position)

name = input("Enter an email : ")
value = 0
if "@" in name:
    start = name.find("@")
    for i in range(start,len(name)):
        if name[i] == ".":
            value += 1
    if value == 1:
        print("Valid Email :",name)
    else:
        print("Invalid Email :",name)
else:
    print("Invalid email.\n{}\nEmail must be contain one'@'".format(name))
