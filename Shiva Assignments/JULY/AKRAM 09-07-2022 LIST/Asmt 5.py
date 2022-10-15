# 5. WAP to calculate factorial of even number and table of odd number in the list?

list1 = []
for i in range (2,11,2):
    fact = 1
    for j in range (i,0,-1):
        fact = fact * j
    list1.append("{}!={}".format(i,fact))
print("Factorial of Even Numbers : \n"+str(list1))
for i in range (1,10,2):
    list2 = []
    for j in range (1,11):
        list2.append(i * j)
    print("Table of",i,"=",list2)
