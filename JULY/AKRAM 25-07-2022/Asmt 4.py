# 4. WAP to calculate compound interest using no return type function.

p = int(input("Enter the principle Balance (P) :"))
r = int(input("Enter the annual rate of interest (r) :"))
t = int(input("Enter the time period in years (t) :"))
n = int(input("Enter the no of years the money is compounded(n) :"))

def compoundInterest(p,r,t,n):
    r = r / 100
    compound_interest = p * (1 + (r/n))**(n * t)
    print("Compound interest = %.2f"%compound_interest)

compoundInterest(p,r,t,n)