# 17. Write a program in Python to remove duplicate items from a list.

list1 = [1,2,3,4,2,5,6,4,7,8,2,9,3,10]
for i in range (len(list1)):
    print(list1[i],end=" ")
    if 4 % 4 == 0:
        list1.remove(4)
        break
print(list1)