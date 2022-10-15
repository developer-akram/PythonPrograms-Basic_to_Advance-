# 10. Write a program to reverse a list in Python.

list1 = ["Akram","Khan",44,5.24,450,"West Bengal",33,56.41,"I love you",14]
print("Original : ")
print(list1)
print("Reverse [Easy Method] : ")
print(list1[::-1])
print("Reverse [Difficult Method] : ")
list2 = []
for i in range (len(list1),0,-1):
    for j in range (i):
        list2.append(list1[i-1])
        break
print(list2)