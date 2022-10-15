# 1. Reverse the tuple

a = (5,4,3,2,1,7,8,9,6)
x = []
print("Original :",a)
for i in a:
    x.insert(0,i)
print("Reverse :",tuple(x))