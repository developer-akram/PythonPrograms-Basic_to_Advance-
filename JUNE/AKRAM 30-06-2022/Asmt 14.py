# 14. Write a   program to check whether a number is Perfect number or not.
# 6, 28, 496, 8128

num = int(input("Enter any number : "))
i = 1
count = 0
while i < num :
    if num % i == 0 :
        count += i
    i += 1
if count == num :
    print(num,"is a perfect number.")
else:
    print(num,"is not a perfect number.")