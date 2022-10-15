mob = int(input("Enter mobile number : "))
x = mob
y = mob
if len(str(mob)) == 10:
    max = 0
    sec_max = 0
    third_max = 0
    while mob != 0:
        r = mob % 10
        mob = mob // 10
        if r > max:
            max = r
    print("First Max =",max)
    while x != 0:
        r = x % 10
        x = x // 10
        if r > sec_max and r != max:
            sec_max = r
    print("Second Max =",sec_max)
    while y != 0:
        r = y % 10
        y = y // 10
        if r > third_max and r != max and r != sec_max:
            third_max = r
    print("Third Max =",third_max)

else:
    print("Mobile number should be 10 digits")