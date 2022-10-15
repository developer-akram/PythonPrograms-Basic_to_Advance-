# 11. Python program to remove a set of keys.

a = {1: 'Value 1', 2: 'Value 2', 3: 'Value 3'}
print("Given Dictionary :",a)
print("Choose a key from : [",end=" ")
for i in a.keys():
    print(i,end=" ")
cut = int(input("] : "))
if cut in a.keys():
    print("[{}: '{}'] Deleted Successfully.".format(cut,a[cut]))
    del a[cut]
    print("Updated dictionary :",a)
else:
    print("Key is not found in Dictionary")