# 33. Write a python program to read a number and print the binary of that number

num = int(input("Enter a number : "))
binary = 0
while num > 0:
    r = num % 2
    binary = binary * 10 + r
    num = num // 2
else:
    print("Binary number :",binary)