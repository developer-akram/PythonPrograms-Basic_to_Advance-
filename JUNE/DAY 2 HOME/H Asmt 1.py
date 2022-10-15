#----------------------------------------H ASSIGNMENT 1-----------------------------------------------------
# WAP to calculate the total salary of an employee where basic, ta, da, comm, pf,hra, leave will be entered by the users?

basic_salary = int(input("Enter the basic salary of the Employee : "))
allow_travel = int(input("Enter travelling allowance of the Employee : "))
allow_dearness = int(input("Enter dearness allowance of the Employee : "))
communications = int(input("Enter the communication bill of the Employee : "))
user_pf = int(input("Enter amount of provident fund of the Employee : "))
user_h_rent_a = int(input("Enter the house rent allowance of the Employee : "))
user_leaves = int(input("Enter the no of leaves the Employee : "))

total_salary = basic_salary + allow_travel + allow_dearness + communications + user_pf + user_h_rent_a
deduction = (total_salary/30) * user_leaves
gross_salary = total_salary - user_pf - deduction
print("The total salary of the Employee is : {0}/-".format(total_salary))
print("The total no of leaves = {0}/-,deduction of the Employee is : {1}/-".format(user_leaves,deduction))
print("The gross salary of the Employee is : {0}/- and the pf amount : {1}/-".format(gross_salary,user_pf))
