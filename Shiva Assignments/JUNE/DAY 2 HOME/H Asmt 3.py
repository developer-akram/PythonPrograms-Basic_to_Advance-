# ----------------------------------------H ASSIGNMENT 3----------------------------------------------
#3) WAP to calculate Simple Interest where rate and time will be constant and the principal will be an integer?

rate_of_interest = 8
time_duration = 3
print("Rate of interest = {0}% and Time duration = {1} years".format(rate_of_interest,time_duration))
p_amount = int(input("Enter the amount to check it's Simple interest : "))
simple_interest = (p_amount * rate_of_interest * time_duration) / 100
print("Simple interest of {0} = {1}".format(p_amount,simple_interest))
