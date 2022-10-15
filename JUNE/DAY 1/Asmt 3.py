#---------------------------------------------ASSIGNMENT 3-----------------------------------------
# If the marks obtained by a student in five different subjects are input through the keyboard,
# find out the aggregate marks and percentage marks obtained by the student.
# Assume that the maximum marks that can be obtained by a student in each subject is 100.

sub_1 = int(input("Enter the marks between 0 to 100 of Subject 1 : "))
sub_2 = int(input("Enter the marks between 0 to 100 of Subject 2 : "))
sub_3 = int(input("Enter the marks between 0 to 100 of Subject 3 : "))
sub_4 = int(input("Enter the marks between 0 to 100 of Subject 4 : "))
sub_5 = int(input("Enter the marks between 0 to 100 of Subject 5 : "))
total = sub_1 + sub_2 + sub_3 + sub_4 + sub_5
percentage  = total/5

print("Aggregate marks = ",total,"out of 500")
print("Percentage = ",percentage)
