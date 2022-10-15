# 12. Write a program to sort the given array

a = [4,4,7,3,78,9,2,1,6,25]
print("Given array :",a)
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] > a[j]:
            a[i],a[j] = a[j],a[i]
print("Sorted array :",a)