#show table if number is composite otherwise display facorial
x =int(input("Enter number :"))
i = 1
c = 0
while(x >= i):
    if x % i == 0:
        c += 1
    i += 1
if x == 1 or c == 2:
    print(x,"is not a composite number.")
    i = 1
    while (i < 11):
        print("{0} * {1} = {2}".format(x, i, x * i))
        i += 1
else:
    print(x,"is a composite number.")
    f = 1
    while (x > 0):
        if x != 1:
            print(x,end=" * ")
        else:
            print("1 = ",end="")
        f = f * x
        x -= 1
    print(f)