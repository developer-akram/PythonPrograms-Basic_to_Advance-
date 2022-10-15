# 1. WAP to reverse a five-digit number using the no return type function.

def reverse_5_digit():
    a = int(input("Enter a 5 digit number : "))
    if a > 9999 and a < 100000:
            x = str(a)
            print(f"Reverse of {a} = {x[::-1]}")
    else:
        print("Number should be five digits")

reverse_5_digit()