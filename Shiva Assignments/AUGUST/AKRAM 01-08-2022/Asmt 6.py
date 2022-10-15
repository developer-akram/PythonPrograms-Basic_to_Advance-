# 6. Find common elements in three sorted arrays

import listint_union_inter_common as mylist
a = mylist.list_int()
a.sort()
b = mylist.list_int()
b.sort()
c = mylist.list_int()
c.sort()
final = a,b,c
print(f"Given list :\n{a}\n{b}\n{c}")
result = mylist.common(*final)
print("Common elements are :",result)