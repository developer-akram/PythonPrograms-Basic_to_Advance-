# 3. WAP to calculate the greatest number using a ternary operator in Python?

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

x = "a is greatest" if a>c else "c is greatest" if a>b \
    else "b is greatest" if b>c else "c is greatest"
print(x)