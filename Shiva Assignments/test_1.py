a=input()
b=input()
try:
    a=complex(a)
    b = complex(b)
except Exception:
    pass
print(type(a))
try:
    a= float(a)
    b = float(b)
except Exception:
    pass
print(type(a))
try:
    a=int(a)
    b = int(b)
except Exception:
    pass
print(type(a))
print(type(b))
choice = input("Choose Operation:\n[+] for Add\n[-] for Sub\n[*]"
               " for Mul\n[/] for division :")
if type(a)!=str and type(b) != str:
    if choice == "+":
        print(f"{a} + {b} = {a+b}")
    if choice == "-":
        print(f"{a} - {b} = {a-b}")
    if choice == "*":
        print(f"{a} * {b} = {a*b}")
    if choice == "/":
        print(f"{a} / {b} = {a/b}")
else:
    print("Invalid Number")



