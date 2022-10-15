# 11. OUTPUT :
# A a B b C
# A a B b
# A a B
# A a
# A

for i in range (6,1,-1):
    k = 65
    for j in range (1,i):
        if j % 2 != 0:
            print(chr(k),end=" ")
        else:
            print(chr(k+32),end=" ")
            k = k + 1
    print()