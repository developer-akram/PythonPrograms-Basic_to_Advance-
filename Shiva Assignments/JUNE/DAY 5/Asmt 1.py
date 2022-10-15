# ----------------------------------------ASSIGNMENT 1------------------------------------------
# Write a program to calculate area of a triangle using herons formula.

side_1 = int(input("Enter the length of side 1 : "))
side_2 = int(input("Enter the length of side 2 : "))
side_3 = int(input("Enter the length of side 3 : "))

s = ( side_1 + side_2 + side_3 ) / 2
area = ( s*(s-side_1) * (s-side_2) * (s-side_3) )**0.5
print("Area of the Triangle =",area)