# 5. WAP to sort the array elements in ascending order?
a = []
def myfunc(mylist):
    mylist = mylist.split(" ")
    mylist = list(map(int,mylist))
    return mylist
choice = input("choose the order of matrix : ")
myrange = myfunc(choice)
for i in range(myrange [0]):
    nos = input(f"enter {myrange[1]} values of row [{i+1}] : ")
    a = a + myfunc(nos)
def showmatrix():
    index = 0
    for i in range (myrange[0]):
        for j in range(myrange[1]):
            print(a[index],end=" ")
            index += 1
        print()
print("Your input matrix : ")
showmatrix()
a.sort()
print("Your Sorted matrix : ")
showmatrix()
