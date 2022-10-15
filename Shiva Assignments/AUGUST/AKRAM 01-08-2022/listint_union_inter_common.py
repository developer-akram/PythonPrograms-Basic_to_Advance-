def list_int():
    mylist = input("Type numbers separated by space : ")
    mylist = mylist.split(" ")
    mylist = list(map(int, mylist))
    return mylist
def union(list1, list2):
    c = list1.copy()
    for i in list2:
        if i not in c:
            c.append(i)
    return c
def intersection(first, second):
    global inter
    inter = []
    for i in first:
        if i in second:
            inter.append(i)
    return inter

def common(*lists):
    intersection(lists[0],lists[1])
    for i in range(2,len(lists)):
        for j in inter:
            if j not in lists[i]:
                inter.remove(j)
    return inter