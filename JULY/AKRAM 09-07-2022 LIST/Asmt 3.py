# 3. WAP to find max elements in list?
a = [10, 11, 5, 15, 7, 22, 28, 4, 17, 18,]
for i in range (1,len(a)):
    if a[i-1] > a[i]:
        a[i] = a[i-1]
print(a[i])