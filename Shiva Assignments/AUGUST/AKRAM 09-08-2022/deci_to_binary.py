# Decimal to binary

num = int(input("Enter decimal number : "))
binary = ""
while num != 0:
    r = num % 2
    binary = str(r)+ binary
    num //= 2
print("Binary number =",binary)