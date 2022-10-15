# 32. 4. Write a python program to get the following output
# 1-----99
# 2-----98
# 3-----97
# .
# .
# 98-----2
# 99-----1

for i in range (99,0,-1):
    for j in range (100-i,100):
        print("{}-------{}".format(j,i))
        break
