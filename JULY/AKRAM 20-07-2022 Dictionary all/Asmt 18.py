# 18. Write a program to sort dictionary values in python.

a = {"fruit 1":"ball","fruit 2":"aam","fruit 3":"orange","fruit 4":"lichi"}
print("Given Dictionary :\n",a)
b = list(a.values())
b.sort()
c = {}
for i in b:
    for k, v in a.items():
        if v == i:
            c[k] = v
            break
print("After Sorting :\n",c)
