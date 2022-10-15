# 10. WAP to find the max element in a set not using max()?

a = set([545,35,767,232,775,244,375,763])
print("Input set :",a)
max = 0
for i in a:
    if i > max:
        max = i
print("Maximum value in the set =",max)