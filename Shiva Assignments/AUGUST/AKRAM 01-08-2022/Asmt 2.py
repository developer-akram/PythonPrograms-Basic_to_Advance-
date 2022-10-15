# 2.Sort the array of 0s, 1s, and 2s

a = [ 0, 1, 2, 5, 9, 8, 5, 2, 0, 1, 0, 2, 1, 0 ]
print("Given array :",a)
mylist = [0,1,2]
for i in a[:]:
    if i not in mylist:
        a.remove(i)
size = len(a)
for i in range (size):
    for j in range (i+1,size):
        if a[i] > a[j]:
            a[i],a[j] = a[j],a[i]
print("Sorted by 0s 1s 2s :",a)