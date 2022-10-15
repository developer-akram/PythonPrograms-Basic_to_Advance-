# 7. WAP to print only duplicate elements in the array and it should display once?

a = [1,2,2,4,5,6,4,7,8,3,5,8,3]
mylist = []
print("Given array :",a)
print("Repeated elements are :")
for i in a:
    if a.count(i) > 1:
        if i not in mylist:
            print(i,end=" ")
            mylist.append(i)
