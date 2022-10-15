#1. W a p to input minimum range and maximum range and check all the armstrong numbers between the range and display it

min_range = int(input("Enter a minimum range : "))
max_range = int(input("Enter a maximum range : "))
num = min_range
while num >= min_range and num < max_range:
    d = 0
    a = b = num
    armstrong = 0
    while a > 0:
        d += 1
        a //= 10
    while b > 0:
        r = b % 10
        armstrong +=  r ** d
        b //= 10
    if armstrong == num:
        print(num)
    num += 1