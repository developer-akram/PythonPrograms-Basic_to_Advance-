# 12.WAP to display prime element in Set?

a = {1,22,3,5,6,35,674,33,56,24,67,73,41,22,59}
print("Input set :",a)
x = set({})
for i in a:
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        x.add(i)
print("Prime elements are :",x)

