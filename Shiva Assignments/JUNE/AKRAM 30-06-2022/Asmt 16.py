# 16. Write a   program to check whether a number is Strong number or not.
#145, 40585

num = int(input("Enter a number : "))
strong = 0
new = num
while num > 0 :
    r = num % 10
    x = 1
    num //= 10
    while r > 0 :
        x = x * r
        r -= 1
    strong += x
if strong == new:
    print(new,"is a Strong Number")
else:
    print(new,"is Not a Strong Number")