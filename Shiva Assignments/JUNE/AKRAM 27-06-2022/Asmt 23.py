# 23. Write a program to input marks of five subjects Physics, Chemistry, Biology,
# Mathematics and Computer. Calculate percentage and grade according to following:
# Percentage >= 90% : Grade A
# Percentage >= 80% : Grade B
# Percentage >= 70% : Grade C
# Percentage >= 60% : Grade D
# Percentage >= 40% : Grade E
# Percentage < 40% : Grade F

phy = int(input("Enter the marks of Physics out of 100 : "))
che = int(input("Enter the marks of Chemistry out of 100 : "))
math = int(input("Enter the marks of Mathematics out of 100 : "))
bio = int(input("Enter the marks of Biology out of 100 : "))
com = int(input("Enter the marks of Computer out of 100 : "))

total = (phy + che + math + bio + com)
average = (total / 5)
percentage = (total /5)
print("Percentage = %.2f"%percentage)
if percentage >= 90 :
    print("GRADE A")
else :
    if percentage >= 80 :
        print("GRADE B")
    else :
        if percentage >= 70 :
            print("GRADE C")
        else:
            if percentage >= 60 :
                print("GRADE D")
            else:
                if percentage >= 40:
                    print("GRADE E")
                else:
                    print("GRADE F")
