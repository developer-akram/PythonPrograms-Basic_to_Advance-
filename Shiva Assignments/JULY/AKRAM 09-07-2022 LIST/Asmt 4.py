# 4. WAP to arrange list elements
print("1. Easy Method : ")
a = [1,2,3,1,1,5,2,3,4,5]
a.sort()
print(a)
print("2. Difficult Method : ")
for i in range (1,len(a)):
    if a[i-1] > a[i]:
        temp = a[i]
        a[i] = a[i-1]
        a[i-1] = temp
print(a)


