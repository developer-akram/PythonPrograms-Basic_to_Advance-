# 4. Write a program to perform the addition of a one-digit positive number?

sum = 0
i = 1
ans = ""
while i < 10:
    sum = sum + i
    if i < 9 :
        ans = ans + str(i) + " + "
    else:
        ans = ans + str(i) + " ="
    i = i + 1
print(ans,sum)