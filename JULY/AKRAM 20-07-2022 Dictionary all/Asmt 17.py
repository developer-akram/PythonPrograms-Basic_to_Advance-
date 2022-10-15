# 17. Write a program in Python to check whether value is exist or not in dictionary.

a = {"key 1":11,"key 2":22,"key 3":33,"key 4":44}
print("Dictionary :",a)
val = int(input("Enter a value : "))
if val in a.values():
    print("Value exist in Dictionary")
else:
    print("Value not exist in Dictionary")