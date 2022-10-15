list1 = [11, 13, 2, 9, 5, 61, 4]
list2 = {11, 13, 2, 9, 5, 61, 4}
list3 = (11, 13, 2, 9, 5, 61, 4, 2, 22, 2)
list4 = (1,)
print(type(list1))
print(type(list2))
print(type(list3))
list1.append(22)
#list1.remove(9)
list1.count(5)
list1.insert(1, 69)
print(list1)
print(list3.count(2))
print(list3.index(61))
#del list3
print(list3)
print(list4)