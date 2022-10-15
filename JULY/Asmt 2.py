# 2. Write a program to perform all aerthmetic opertaion using functions
global a, b


def InputValues():
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
def Addition():
    print(f"Addition : {a} + {b} = {a + b}")
def Substraction(a,b):
    if b > a:
        a,b = b,a
    print(f"Substraction : {a} - {b} = {a - b}")
def Multiplication():
    print(f"Multiplication : {a} * {b} = {a * b}")
def Division():
    if b > a:
        a,b = b,a
    print(f"Division : {a} / {b} = %.2f"%(a / b))
def TrueDivision():
    if b > a:
        a,b = b,a
    print(f"True-Division : {a} // {b} = {a // b}")
def Modulus():
    print(f"Division : {a} % {b} = {a % b}")
#InputValues()
while True:
    print("[1] for Addition\t[2] for Substraction\t[3] for Multiplication"
          "\n[4] for Division\t[5] for TrueDivision\t[6] for Modulus\n[7] for Exit")
    me = int(input("Choose your option : "))
    if me == 1:
        Addition()
    elif me == 2:
        Substraction(a,b)
    elif me == 3:
        Multiplication()
    elif me == 4:
        Division(a,b)
    elif me == 5:
        TrueDivision(a,b)
    elif me == 6:
        Modulus()
    elif me == 7:
        break
    else:
        print("Your choice should be in between 0 to 6")