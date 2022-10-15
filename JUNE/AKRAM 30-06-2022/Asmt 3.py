# 3. WAP to calculate factorial of a number with complete expression?

num = int(input("Enter any number : "))
i = 1
ans = ""
while num > 0:
    i = i * num
    if num > 1:
        ans = ans + str(num) + " * "
    else:
        ans = ans + str(num) + " = "
    num -= 1
print(ans,i)