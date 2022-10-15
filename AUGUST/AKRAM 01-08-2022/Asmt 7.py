# 7. Find if there is any subarray with sum equal to zero

a = [[1,-2,3,-2],[4,25,6,3],[4,5,22,5,-36],[2,4,6,7]]
print("Given array :")
[print(i,end=" ")for i in a]
print("\nSubarray with [sum = 0] present is position :",end=" ")
for i in a:
    sum = 0
    for j in i:
        sum += j
    else:
        if sum == 0:
            print(f"{a.index(i)+1}",end=" ")