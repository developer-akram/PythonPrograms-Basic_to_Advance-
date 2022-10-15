# 6. Write a program to check whether a given key exists in a dictionary or not.

a = {"a":"Akram","g":"Ganesh","v":"Vrushank","m":"Mukesh","N":"Neha"}
print("Input Dictionary :",a)
name = input("Enter an item : ")
for i,j in a.items():
    if i == name:
        print("Key found!\n{} for {}".format(i,j.upper()))
        break
else:
    print("Key not found in Dictionary")