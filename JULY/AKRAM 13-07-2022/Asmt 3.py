# 3. Write a program to reverse the list

a = [5,4,3,2,1]
b = []
for i in range (len(a)-1,-1,-1):
    b.append(a[i])
print(b)