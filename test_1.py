# S = 1 + 4 – 9 + 16 – 25 + 36 – … … n

n = int(input("Enter range : "))
i = 1
s = ""
sum = 0
while i <= n :
    if i % 2 != 0 :
        s = s + str(i**2) + " + "
        sum= sum + i**2
    else:
        s = s + str(i**2) + " - "
        sum = sum + (-i**2)
    i = i + 1
print(s,sum)