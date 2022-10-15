# 19. WAP to calculate factorial of a number with complete expression?

num = int(input("Enter a number : "))
fact = 1
while num >= 1:
    print(num,end=" * ")
    fact = num * fact
    num -= 1
print("=",fact)