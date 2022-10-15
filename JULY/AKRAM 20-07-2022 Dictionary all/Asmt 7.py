# 7. Write a program to iterate over dictionary items using for loop.

size = int(input("Enter dictionary size : "))
a = {}
for i in range (size):
    a[i+1] = int(str(i+1)+"000")
print(a)
for key, value in a.items():
    print("Key = {}\tvalue = {}".format(key,value))
