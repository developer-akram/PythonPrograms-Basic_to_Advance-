# 13. Python program to append an element to a list.

list1 = ["Hello", 34, 45, 40, 4.12]
print("Before Append :",list1)
num = int(input("How many values you want to append : "))
for i in range (num):
    a = input("Input value {} : ".format(i+1))
    list1.append(a)
print("After Append : ",list1)