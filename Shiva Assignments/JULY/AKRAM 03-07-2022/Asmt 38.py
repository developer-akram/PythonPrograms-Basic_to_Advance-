# 38. a, b, c = 0, 0, 0 . Write a python program to print all permutations using those three variables
# Output : 000 , 001 ,002, 003, 004, 0005 ,006, 007, 008, 009, 010, 011 …… 999
for i in range (10):
    for j in range (10):
        for k in range (10):
            if i == 9 and j == 9 and k == 9 :
                print("{}{}{}".format(i, j, k), end="")
            else:
                print("{}{}{}".format(i,j,k),end=", ")
