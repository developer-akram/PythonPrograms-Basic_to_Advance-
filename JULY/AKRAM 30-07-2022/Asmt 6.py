# 6. WAP to find second max, first max, and third max elements
# in an array without sorting?

a = [1,7,3,6,2,8,8,9,3,5]
print("Givenn array :",a)
max = a[0]
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
else:
    print("First Max :",max)
sec_max = a[0]
for i in range(len(a)):
    if a[i] > sec_max and a[i] != max:
        sec_max = a[i]
else:
    print("Second Max :",sec_max)
third_max = a[0]
for i in range(len(a)):
    if a[i] > third_max and a[i] != max and a[i] != sec_max:
        third_max = a[i]
else:
    print("Third Max :",third_max)