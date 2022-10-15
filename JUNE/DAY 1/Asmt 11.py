#--------------------------------------------ASSIGNMENT 11------------------------------------------
# Write a program to enter radius of a circle and find its diameter, circumference and area.

circle_radius = int(input("Enter the radius of Circle : "))
circle_area =(22/7)*(circle_radius**2)
circle_circumference = 2*(22/7)*circle_radius
circle_diameter = circle_radius*2
print("The diameter of the Circle = {0}\nThe circumference of the Circle = {1}\nThe area of the Circle = {2}"
      .format(circle_diameter,circle_circumference,circle_area))