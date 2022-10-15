# 3. WAP to create a salary calculator using no return type function

b = int(input("Enter the basic salary : "))
t = int(input("Enter travalling assurance amount : "))
hr = int(input("Enter house rental assurance : "))
pf = int(input("Enter pf amount :"))

def salary (b,t,hr,pf):
    total = b + t + hr + pf
    gross = total - pf
    print("Total salary :",total)
    print("Gross salary :",gross)

salary(b,t,hr,pf)