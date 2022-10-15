#1.WAP to Display Prime elements in List?

ranged = int(input("Enter a range : "))
a = []
for i in range (1,ranged):
        for j in range (2,i):
            if i % j == 0:
                break
        else:
            a.append(i)
print("\t\t[ 1 to",ranged,"]\nPrime numbers are :",a)