# 13. Write a program to concatenate two dictionaries to create one.

a = {"key 1":2,"key 2":3}
b = {"key 3":4,"key 4":5}
print("Dict1 :{}\nDict2 :{}".format(a,b))
for i,j in b.items():
    a[i] = j
print("Concationate :",a)