# 9. Check if all items in the tuple are the same
a = (1,2,3,"4")
b = (1,2,3,'4')
count = 0
if len(a) == len(b):
    for i in range (len(a)):
        if a[i] == b[i]:
            print("{} |[A]| ITEM |[B]| {}".format(a[i],b[i]))
            count  += 1
        else:
            print("Item no {} is not same.So,tuples are not same".format(i+1))
            break
    if count == len(a):
        print("Tuples are same so,all items are equal")
else:
    print("Tuples are not same")

