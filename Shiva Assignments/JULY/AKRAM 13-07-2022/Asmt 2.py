# 2. Find the minimum and maximum element in an list

list1 = [5,4,3,2,1,7,8,9,6]
for i in range (len(list1)):
    for j in range (len(list1)):
        if list1[i] > list1[j]:
            list1[i],list1[j] = list1[j],list1[i]

print("Minimum Element =",list1[len(list1)-1])
print("Maximum Element =",list1[0])
