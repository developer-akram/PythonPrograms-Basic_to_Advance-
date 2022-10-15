# 20. Write a program in python to map keys to dictionary.
# key = [‘Fruit’, ‘Vegetable’] value = [‘Mango’,’Tomato’]

key = ["Fruit","Vegetable"]
value = ["Mango","Tomato"]
print("Key = {}\nvalue = {}".format(key,value))
a = {}
if len(key) == len((value)):
    for i in range (len(key)):
        a[key[i]] = value[i]
print("Dictionary :",a)