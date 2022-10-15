# 6. WAP to calculate the sum of one digit positive number using for else

sum = 0
for i in range (1, 10):
    if i == 9:
        print("{} = ".format(i), end="")
    else:
        print("{} + ".format(i),end="")
    sum = sum + i
else:
    print(sum)