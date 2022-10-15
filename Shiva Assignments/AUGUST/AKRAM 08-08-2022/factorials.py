n = int(input("Enter number : "))
text = ""
f = 1
while ( n > 0):
    f = f * n
    text = text + str(n) + " * "
    if n == 2:
        break
    n -= 1
print(text+"1 =",f)