# 17. Write a  program to print all Strong numbers between 1 to n.

range = int(input("Enter a range : "))
check_all = 1
while check_all <= range:
    num = check_all
    strong = 0
    while num > 0 :
        r = num % 10
        x = 1
        num //= 10
        while r > 0 :
            x = x * r
            r -= 1
        strong += x
    if strong == check_all:
        print(check_all)
    check_all += 1
