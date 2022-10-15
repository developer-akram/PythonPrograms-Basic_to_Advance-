# 5. WAP to check the prime number?

num = int(input("Enter any number : "))
i = 1
count = 0
while i <= num :
    if num % i == 0 :
        count += 1
    i += 1
if count == 2:
    print(num,"is a Prime number.")
else:
    print(num,"is Not a Prime number.")