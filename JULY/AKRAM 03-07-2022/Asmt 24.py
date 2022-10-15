# 24. Accept a number and check whether it is palindrome or not.

num = int(input("Enter a number : "))
new = check = num
digit = 0
palin = 0
while num > 0 :
    num //=10
    digit = digit + 1
for i in range (digit):
    r = new % 10
    palin = palin * 10 + r
    new //= 10
if palin == check :
    print(check,"is a Palindrome number.")
else:
    print(check,"is not a Palindrome number.")