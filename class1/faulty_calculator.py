# 45*3 = 355, 56+9 = 77, 56/6 = 4
num1 = int(input("Enter first Number : "))
num2 = int(input("Enter second Number : "))
oper = input("Choose an operation from the following : \nAddition [+]\nSubstraction [-]\nMultiplication [*]"
                 "\nDivision [/]\nPower [**]\nModule [%]\nEnter your Choice : ")
if oper == "+":
    if num1 == 56 and num2 == 9:
        print("56 + 9 = 77")
    else :
        print("{} + {} = {}".format(num1, num2, num1+num2))
elif oper == "*":
    if num1 == 45 and num2 == 3:
        print("45 * 3 = 355")
    else :
        print("{} * {} = {}".format(num1, num2, num1*num2))
elif oper == "/":
    if num1 == 56 and num2 == 6:
        print("56 / 6 = 4")
    else :
        print("{} / {} = {}".format(num1, num2, num1/num2))
elif oper == "-":
    print("{} - {} = {}".format(num1, num2, num1-num2))
elif oper == "** ":
    print("{} ** {} = {}".format(num1, num2, num1**num2))
elif oper == "%":
    print("{} % {} = {}".format(num1, num2, num1%num2))
else :
    print("You entered an invalid option,Please try again.")