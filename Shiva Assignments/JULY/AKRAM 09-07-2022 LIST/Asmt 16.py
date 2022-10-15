# 16. Write a program to get the maximum number from a list.

list1 = [10, 11, 5, 15, 7, 22, 28, 4, 17, 18, ]
for i in range (1, len(list1)):
    if list1[i - 1] > list1[i]:
        list1[i] = list1[i - 1]
print(list1[i])