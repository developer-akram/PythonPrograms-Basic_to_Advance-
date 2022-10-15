# 12. Python program to remove an empty element from a list.

list1 = ["Hello", 34, 45, "", 40]
print("Input : ",list1)
for i in list1:
    if i == "":
        list1.remove(i)
print("Output :",list1)