#-------------------------------------------ASSIGNMENT 15-----------------------------------------
# Write a   program to convert days into years, weeks and months.

days = int(input("Enter the no of days : "))

print("{} days converted into {}".format(days,days//7),"weeks")
print("{} days converted into {}".format(days,days//30),"months")
print("{} days converted into {}".format(days,days//365),"years")

