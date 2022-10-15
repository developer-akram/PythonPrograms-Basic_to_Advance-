import random

def matrix(order,minimum,maximum):
    rowlist = []
    x = y = z = d = 0
    for i in range (order):
        m = 0
        for j in range (order):
            no = random.randint(minimum, maximum)
            print(no, end="    ")
            if i == j :
                d += no
            if j == 0:
                x += no
            if j == 1:
                y += no
            if j == 2:
                z += no
            if i >= 0:
                m += no
        else:
            rowlist.append(m)
            print(f"\tSum = {rowlist[i]}")
            print()
    else:
        if i == 2:
            print("Sum  Sum  Sum")
            print(f"{x}   {y}   {z}")
        else:
            print("Sum  Sum")
            print(f"{x}   {y}")
    print("\nHeightest sum in row :",max(rowlist))
    print("Heightest sum in column :",max(x,y,z))
    print("Sum of diagonal matrix :",d)


