# 5. Find the Kth largest and Kth smallest number in an list
a = [5, 4, 3, 2, 1, 7, 8, 9, 6]
for i in range (len(a)):
    for j in range (len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
for i in range (len(a)):
    if a[0] > a[i]:
        print("Second largest element :", a[i])
        break
for i in range (len(a)):
    for j in range (len(a)):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]
for i in range (len(a)):
    if a[0] < a[i]:
        print("Second smallest element :", a[i])
        break