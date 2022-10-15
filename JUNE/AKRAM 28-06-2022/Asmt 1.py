# 1. WAP to Calculate Marksheet using five different subjects with the following condition.
# 1) all subject marks should be 0 to 100.
# 2) if only one subject mark is <33 then the student will be suppl.
# 3) if all subject marks are >=33 then percentage and division should be calculated.
# 4) if a student is suppl then five bonus marks can be applied to be pass and the result will be "pass by grace".
# 5) Display Grace Subject name, distinction subject name, suppl subject name, and failed subject name.

math = int(input("Enter the mark of MATHEMATICS : "))
phy = int(input("Enter the mark of PHYSICS : "))
chem = int(input("Enter the mark of CHEMISTRY : "))
bio = int(input("Enter the mark of BIOLOGY : "))
comp = int(input("Enter the mark of COMPUTER : "))
if math >= 0 and phy >= 0 and chem >= 0 and bio >= 0 and comp >= 0 and \
   math  <= 100 and phy <= 100 and chem <= 100 and bio <= 100 and comp <= 100:
    if math > 90 :
        print("Congrats! You got distinction in MATHEMATICS ")
    if phy > 90:
        print("Congrats! You got distinction in PHYSICS ")
    if chem > 90:
        print("Congrats! You got distinction in CHEMISTRY ")
    if bio > 90:
        print("Congrats! You got distinction in BIOLOGY ")
    if comp > 90:
        print("Congrats! You got distinction in COMPUTER ")
    if math <= 33 or phy <= 33 or chem <= 33 or bio <= 33 or comp <= 33:
        if math < 28 and phy < 28 or math < 28 and chem < 28 or math  < 28 and bio < 28 or\
                math < 28 and comp < 28 or phy < 28 and chem < 28 or phy < 28 and bio < 28 or\
                phy < 28 and comp < 28 or chem < 28 and bio < 28 or chem < 28 and comp < 28 or\
                bio < 28 and comp < 28 :
            if math <28:
                print("Oops! You failed in MATHEMATICS ")
            if phy < 28:
                print("Oops! You failed in PHYSICS ")
            if chem < 28:
                print("Oops! You failed in CHEMISTRY ")
            if bio < 28:
                print("Oops! You failed in BIOLOGY ")
            if comp < 28:
                print("Oops! You failed in COMPUTER ")
        elif math < 28:
            print("Oops! You got Supply in MATHEMATICS.can't apply for grace because you got = ",math)
        elif phy < 28:
            print("Oops! You got Supply in PHYSICS.can't apply for grace because you got = ",phy)
        elif chem < 28:
            print("Oops! You got Supply in CHEMISTRY.can't apply for grace because you got = ",chem)
        elif bio < 28:
            print("Oops! You got Supply in BIOLOGY.can't apply for grace because you got = ",bio)
        elif comp < 28:
            print("Oops! You got Supply in COMPUTER.can't apply for grace because you got = ",comp)
        print("We cannot provide grades for failed candidates.")
        if math >= 28 and math < 33:
            print("Oops! You got Supply in MATHEMATICS but it will pass by adding grace marks ")
            print("Grace Subject name : MATHEMATICS")
            g_mark = 33 - math
            print("Grace mark in MATH = ", g_mark)
            print("Remember! you will get grace mark in 1 Subject only.")
            math += g_mark
        elif phy >= 28 and phy < 33:
            print("Oops! You got Supply in PHYSICS but it will pass by adding grace marks")
            print("Grace Subject name : PHYSICS")
            g_mark = 33 - phy
            print("Grace mark in PHYSICS = ", g_mark)
            print("Remember! you will get grace mark in 1 Subject only.")
            phy += g_mark
        elif chem >= 28 and chem < 33:
            print("Oops! You got Supply in CHEMISTRY but it will pass by adding grace marks")
            print("Grace Subject name : CHEMISTRY")
            g_mark = 33 - chem
            print("Grace mark in CHEMISTRY = ", g_mark)
            print("Remember! you will get grace mark in 1 Subject only.")
            chem += g_mark
        elif bio >= 28 and bio < 33:
            print("Oops! You got Supply in BIOLOGY but it will pass by adding grace marks")
            print("Grace Subject name : BIOLOGY")
            g_mark = 33 - bio
            print("Grace mark in BIOLOGY = ", g_mark)
            print("Remember! you will get grace mark in 1 Subject only.")
            bio += g_mark
        elif comp >= 28 and comp < 33:
            print("Oops! You got Supply in COMPUTER but it will pass by adding grace marks")
            print("Grace Subject name : COMPUTER")
            g_mark = 33 - comp
            print("Grace mark in COMPUTER = ", g_mark)
            print("Remember! you will get grace mark in 1 Subject only.")
            comp += g_mark
    if math >= 33 and phy >= 33 and chem >= 33 and bio >= 33 and comp >= 33:
        print("GRADE A = [90 - 100]%")
        print("GRADE B = [70 - 89]%")
        print("GRADE C = [50 - 69]%")
        print("GRADE D = [33 - 49]%")
        total = math + phy + chem + bio + comp
        percentage = total / 5
        if percentage >= 90 :
            print("Congrats! You got Grade A")
            print("Your percentage = %.2f"%percentage)
        elif percentage >= 70 :
            print("You got Grade B")
            print("Your percentage = %.2f"%percentage)
        elif percentage >= 50 :
            print("You got Grade C")
            print("Your percentage = %.2f"%percentage)
        elif percentage >= 33 :
            print("You got Grade D")
            print("Your percentage = %.2f"%percentage)
        else:
            print("Your percentage is less than 40.You Fail!")
else:
    print("Each subjects marks should be in between 0 to 100. Please input correct value...")


