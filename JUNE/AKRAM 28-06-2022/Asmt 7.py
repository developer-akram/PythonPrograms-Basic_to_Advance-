# 7. WAP to check the middle number is a three-digit number?

num = int(input("Enter a three digit number : "))

a = num % 10
a1 = num // 10
b = a1 % 10
c = a1 // 10
if a > b and a < c or a < b and a > c :
    print(a," is the middle number")
if b > a and b < c or b < a and b > c :
    print(b," is the middle number")
if c > a and c < b or c < a and c > b :
    print(c," is the middle number")