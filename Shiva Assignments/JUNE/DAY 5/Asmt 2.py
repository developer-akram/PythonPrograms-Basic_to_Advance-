# ----------------------------------------ASSIGNMENT 2------------------------------------------
# Write a program to calculate Compound Interest.

input_p = int(input("Enter the principle Balance (P) :"))
input_r = int(input("Enter the annual rate of interest (r) :"))
input_t = int(input("Enter the time period in years (t) :"))
input_n = int(input("Enter the no of years the money is compounded(n) :"))

input_r = input_r / 100
compound_interest = input_p * (1 + (input_r/input_n))**(input_n * input_t)
print("Compound interest = ",compound_interest)