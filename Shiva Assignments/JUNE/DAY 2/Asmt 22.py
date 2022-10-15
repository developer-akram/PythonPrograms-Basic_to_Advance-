# --------------------------------------ASSIGNMENT 22----------------------------------
# 2.Write a  program to enter P, T, R and calculate Simple Interest.

input_p = int(input("Enter the principle Balance (P) :"))
input_r = int(input("Enter the annual rate of interest (r) :"))
input_t = int(input("Enter the time period in years (t) :"))

simple_interest = (input_p * input_r * input_t) / 100
print("Simple interest = ",simple_interest)