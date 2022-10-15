# 9. Write a program to count the number of items stored in a list.

list1 = ["Akram","Khan",44,5.24,450,"West Bengal",33,56.41,"I love you",14]
print("Easy Method : ")
print("List Size",len(list1))
print("Difficult Method : ")
item = 0
for i in list1:
    item = item + 1
print("There are {} items in the list".format(item))