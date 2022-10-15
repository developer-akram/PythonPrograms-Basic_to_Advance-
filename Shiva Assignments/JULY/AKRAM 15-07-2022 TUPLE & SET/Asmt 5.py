# 5. Swap two tuples in Python

a = (1, 2, 3, 4, 5)
b = (6, 7, 8, 9, 10)
print("Before Swapping \na = {}\nb = {}".format(a,b))
a,b = b,a
print("After Swapping \na = {}\nb = {}".format(a,b))
