# 13. OUTPUT :
# 1 0 0 1 0
# 1 0 0 1
# 1 0 0
# 1 0
# 1

code = "10010"

for i in range (5,0,-1):
    for j in range (i):
        print(code[j],end=" ")
    print()