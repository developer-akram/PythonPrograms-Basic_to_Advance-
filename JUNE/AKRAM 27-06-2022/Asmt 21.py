# 21. Write a program to find all roots of a quadratic equation.

a = int(input("Enter a value : "))
b = int(input("Enter b value : "))
c = int(input("Enter c value : "))

d = (b**2) - (4*a*c)
ans_1 = (-b-(d)**0.5)/(2*a)
ans_2 = (-b+(d)**0.5)/(2*a)

print("The answers are : {0} and {1}".format(ans_1,ans_2))