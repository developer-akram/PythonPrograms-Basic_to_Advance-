# 24. Write a program to input basic salary of an employee and calculate
# its Gross salary according to following:
# Basic Salary <= 10000 : HRA = 20%, DA = 80%
# Basic Salary <= 20000 : HRA = 25%, DA = 90%
# Basic Salary > 20000 : HRA = 30%, DA = 95%

bs = int(input("Enter the basic salary : "))
if bs > 0:
    if bs <= 10000:
        hra = bs * 0.20
        da = bs * 0.80
        gs = bs + hra + da
        print("Gross salary = %.2f"%gs)
    else:
        if bs <= 20000:
            hra = bs * 0.25
            da = bs * 0.90
            gs = bs + hra + da
            print("Gross salary = %.2f"%gs)
        else:
            if bs > 20000 :
                hra = bs * 0.30
                da = bs * 0.95
                gs = bs + hra + da
                print("Gross salary = %.2f"%gs)
else:
    print("Basic salary should be greater than 0")

