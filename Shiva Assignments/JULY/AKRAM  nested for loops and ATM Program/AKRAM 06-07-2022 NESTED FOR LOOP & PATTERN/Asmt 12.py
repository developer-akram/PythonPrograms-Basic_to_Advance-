# 12. OUTPUT :
# 1 2 3 4 5
# 5 4 3 2
# 1 2 3
# 5 4
# 1

x = -1
for i in range(5, 0, -1):
    if i % 2 != 0:
        for j in range(i):
            print(j + 1, end=" ")
    else:
        x = x + 2
        for k in range(5, x, -1):
            print(k, end=" ")
    print()
