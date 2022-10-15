# 2. WAP to perform addition of complex number using return type function

def addition_complex():
    a = complex(input("Enter first complex number : "))
    b = complex(input("Enter second complex number : "))
    return a+b
x = addition_complex()
print("Result is =",x)