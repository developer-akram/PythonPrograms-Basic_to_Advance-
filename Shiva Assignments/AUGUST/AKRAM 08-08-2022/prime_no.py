x =int(input("Enter number :"))
i = 1
c = 0
while(x >= i):
    print(str(x),"/",i)
    if x % i == 0:
        c += 1
    i += 1
if x == 1 or c == 2:
    print("Prime number")
else:
    print("Not a Prime number")