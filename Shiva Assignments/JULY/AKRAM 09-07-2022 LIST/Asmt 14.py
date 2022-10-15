# 14. Write a program to display those items from a list that is divisible by 5.

list1 = [3, 5, 7, 25, 9, 65, 23, 15]
print("Items in list :",list1)
print("Devisible by 5 items are : ",end="")
for i in list1:
    if i % 5 == 0 :
        print(i,end=" ")