# 5. OUTPUT :
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range (5):
    for j in range (i+1):
        print(j+1,end=" ")
    print()