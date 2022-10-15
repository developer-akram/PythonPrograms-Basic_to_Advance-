# 2. W a p to reverse an integer

num = int(input("Enter any number : "))
sum = 0
while num > 0 and num !=0 :
    reminder = num % 10
    sum = sum * 10 + reminder
    num //= 10
print("Reverse =",sum)