# Armstrong

num = int(input("Enter a number : "))
x = num
rev = 0
while num != 0:
    r = num % 10
    rev = rev + r**len(str(x))
    num //= 10
if rev == x:
    print(x,"is an armstrong number.")
else:
    print(x,"is not an armstrong number.")
