# 6. WAP to check divisibility of a number by 3 and 5, individually and both?

num = int(input("Enter a number : "))

x = "Devisible by 3 and 5" if num % 3 ==0 and num % 5 == 0 else "Devisible by 3" if num % 3 == 0 else "Devisible by 5" if num % 5 == 0 else "Not Devisible by 3 and 5"
print(num,x)