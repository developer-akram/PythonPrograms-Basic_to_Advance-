# 8. WAP to split one array into three different subarrays?

a = [1,2,3,4,5,6,7,8,9,10]
print("Given array :",a)
b1,b2,b3 = [],[],[]
div = len(a) // 3
rem = len(a) % 3
x = [div,div,div+rem]
b = [b1,b2,b3]
index = 0
for i in range (len(b)):
    for j in range(x[i]):
        b[i].append(a[index])
        index += 1
print("Output in 3 sub arrys :",b)