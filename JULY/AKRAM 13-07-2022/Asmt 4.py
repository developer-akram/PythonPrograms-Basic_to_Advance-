# 4. Write a program to sort the given list(*)
list1 = [5,4,3,2,1,7,8,9,6]
print("User Given list :",list1)
for i in range (len(list1)):
    for j in range (len(list1)):
        if list1[i] < list1[j]:
            list1[i],list1[j] = list1[j],list1[i]
print("Ascending order :",list1)
for i in range (len(list1)):
    for j in range (len(list1)):
        if list1[i] > list1[j]:
            list1[i],list1[j] = list1[j],list1[i]
print("Descending order:",list1)
