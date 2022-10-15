# 4. Write a program to input three subjects marks and check
# its division or if fail .Display its percentage and its division too.

phy = int(input("Enter mark of Physics :"))
che = int(input("Enter mark of Chemistry :"))
bio = int(input("Enter mark of Bioloy :"))

per = (phy + che + bio) / 3
print("Percentage  = %.2f"%per)
print("Method 1 : Using only IF ")
if per >= 60 :
    print("1st division")
if per >= 50 and per < 60:
    print("2nd division")
if per >= 40 and per < 50:
    print("3rd division")
if per < 40 :
    print("Fail!")

print("Method 2 : Using IF-Else ")
if per >= 60 :
    print("1st division")
else :
    if per >= 50 :
        print("2nd division")
    else :
        if per >= 40 :
            print("3rd division")
        else:
            print("Fail!")


