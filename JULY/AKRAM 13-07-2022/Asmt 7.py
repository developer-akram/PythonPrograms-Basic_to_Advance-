# 7. Move all the negative elements to one side of the list

a = [5, 4, -9, 3, 2, 1,-8, 7, 8, 9, 6,-1,-5,-4,-6]
b = []
print("              User Typed list is :",a)
for i in range (len(a)):
    if a[i] < 0:
        b.insert(0,a[i])
    else:
        b.append(a[i])
print("Negitive and Positive Separation :",b)

c = []
d = []
for i in range (len(a)):
    for j in range (len(a)):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]
for i in range (len(a)):
    if a[i] < 0:
        c.append(a[i])
    else:
        d.append(a[i])
print("Negitive elements in sorted list :",c)
print("Positive elements in sorted list :",d)
