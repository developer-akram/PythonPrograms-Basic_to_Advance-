# 8. Write a program to print only keys of a dictionary.

a = {1:"Value 1", 2:"Value 2", 3:"Value 3"}
print("Given Dictionary :",a)
print("Keys are :",end=" ")
for i in a.keys():
    print(i,end=" ")