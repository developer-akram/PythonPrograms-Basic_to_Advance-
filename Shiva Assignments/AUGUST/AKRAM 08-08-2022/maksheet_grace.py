s1 = int(input("Enter sub1 mark : "))
s2 = int(input("Enter sub2 mark : "))
s3 = int(input("Enter sub3 mark : "))
s4 = int(input("Enter sub4 mark : "))
s5 = int(input("Enter sub5 mark : "))

if (s1 >= 0 and s1 <= 100) and (s2 >= 0 and s2 <= 100) and (s3 >= 0 and s3 <= 100) and (s4 >= 0 and s4 <= 100) and (s5 >= 0 and s5 <= 100):
    c = 0
    x = 0
    l = ""
    if s1 < 33:
        c += 1
        x = s1
        l = "Sub1 " + l
    if s2 < 33:
        c += 1
        x = s2
        l = "Sub2 " + l
    if s3 < 33:
        c += 1
        x = s3
        l = "Sub3 " + l
    if s4 < 33:
        c += 1
        x = s4
        l = "Sub4 " + l
    if s5 < 33:
        c += 1
        x = s5
        l = "Sub5 " + l
    if s1 >= 90 or s2 >= 90 or s3 >= 90 or s4 >= 90 or s5 >= 90 :
        z = ""
        print("Got destingtion in : ",end="")
        if s1 >= 90:
            z ="Sub1" + " = " + str(s1) + " " + z
        if s2 >= 90:
            z ="Sub2" + " = " + str(s2) + " " + z
        if s3 >= 90:
            z ="Sub3" + " = " + str(s3) + " " + z
        if s4 >= 90:
            z ="Sub4" + " = " + str(s4) + " " + z
        if s5 >= 90:
            z ="Sub5" + " = " + str(s5) + " " + z
        print(z)
    if c == 0 or c == 1 and x >=28 :
        per = (s1 + s2 + s2 + s4 + s5) / 5
        if c == 1:
            per += (33-x) / 5
        if per >= 33 and per < 45:
            print("Third division with %.2f"%per,end="")
        elif per < 60:
            print("Second division with %.2f"%per,end="")
        elif per >= 60:
            print("First division with %.2f"%per,end="")
        if c == 1:
            print(" pass by grace")
            print("Grace subject name : {} and Grace marks : {}".format(l,33-x))
    elif c == 1:
        print("Supplymentry in ",l)
    else:
        print("Failed in :",l)
else:
    print("Each subjects marks should in between 0 to 100.")
