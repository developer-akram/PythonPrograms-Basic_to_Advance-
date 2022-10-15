# 5. WAP to check divisibility of number that it is divisible by 3 and 5 or not?

num = int(input("Enter a number : "))
x = "is Devisible by 3 and 5" if num % 3 == 0 and num % 5 == 0 else "is not Devisible by 3 and 5"
print(num,x)