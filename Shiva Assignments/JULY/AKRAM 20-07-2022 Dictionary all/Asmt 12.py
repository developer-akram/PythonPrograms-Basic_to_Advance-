# 12. Python program to sort dictionary by values (Ascending/ Descending).

a = {"abc": 7000, "bcd": 2000, "cde": 6000, "def": 4000, "efg": 5000}
print("Given Dictionary :",a)
b = list(a.values())
b.sort()
c = {}
for i in b:
    for k, v in a.items():
        if v == i:
            c[k] = v
            break
print("Ascending order :",c)
b = b[::-1]
d = {}
for i in b:
    for k, v in a.items():
        if v == i:
            d[k] = v
            break
print("descending order :",d)
