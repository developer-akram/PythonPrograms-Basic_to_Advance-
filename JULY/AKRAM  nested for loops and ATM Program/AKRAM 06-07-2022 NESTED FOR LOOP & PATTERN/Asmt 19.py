# 19. Output :
# A B C D E
# B C D E
# C D E
# D E
# E
k = 65
for i in range (5):
    for j in range (i,5):
        print(chr(j+65),end=" ")
    print()
