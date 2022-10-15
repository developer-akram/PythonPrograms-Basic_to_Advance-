# 5. WAP to calculate factorial of any number with complete expression?

num = int(input("Enter a number : "))
fact = 1
for i in range (num, 1, -1):
    fact = fact * i
    print("{} * ".format(i),end="")
print("1 =",fact)