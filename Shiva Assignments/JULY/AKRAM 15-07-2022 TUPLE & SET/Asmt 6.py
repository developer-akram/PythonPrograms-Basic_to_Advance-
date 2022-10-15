# 6. Copy specific elements from one tuple to a new tuple

a = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print("There are {} items in the tuple\nDefault tuple : {}".format(len(a),a))
size = int(input("How many items you want to copy : "))
b = []
if size <= len(a):
    for i in range (size):
        x = int(input("Enter item {} : ".format(i+1)))
        if x in a:
            b.append(x)
        else:
            print(x, "is not available in the tuple")
    print("Your tuple :",tuple(b))
else:
    print("Copied size is bigger than tuple size")