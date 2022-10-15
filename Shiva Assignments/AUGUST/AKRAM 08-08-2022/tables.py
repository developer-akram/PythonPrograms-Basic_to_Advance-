a = int(input("Enter no to show table : "))
i = 1
while (i < 11 and a > 0):
    print("{} * {} = {}".format(a,i,a*i))
    i += 1