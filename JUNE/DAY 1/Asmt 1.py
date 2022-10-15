#--------------------------------ASSIGNMENT 1-------------------------------------------
# Q1 : Ramesh’s basic salary is input through the keyboard. His dearness allowance is 40% of basic salary,
# and house rent allowance is 20% of basic salary. Write a program to calculate his gross salary

salary_basic = int(input("Enter the Basic Salary of Ramesh  : "))
drns_allow = salary_basic*(0.4)
rent_allow = salary_basic*(0.2)
salary_gross = salary_basic + drns_allow + rent_allow
print("Ramesh Basic Salary is = ",salary_basic)
print("Ramesh dearness allowance is = ",drns_allow)
print("Ramesh house rent allowance is = ",rent_allow)
print("Ramesh Gross Salary is = ",salary_gross)