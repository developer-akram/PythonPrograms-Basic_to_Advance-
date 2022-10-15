# 10. Write a program in python to map 2 lists into a dictionary.

keys = [1,2,3]
values = ["Value 1", "Value 2", "Value 3"]
print("keys : {}\nvalues : {}".format(keys,values))
a = {}
if len(keys) == len(values):
    for i in range (len(keys)):
        a[keys[i]] = values[i]
print("Dictionary :",a)