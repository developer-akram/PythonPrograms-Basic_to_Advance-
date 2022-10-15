#--------------------------------------------ASSIGNMENT 5--------------------------------------------
# The length & breadth of a rectangle and radius of a circle are input through the keyboard.
# Write a program to calculate the area & perimeter of the rectangle,
# and the area & circumference of the circle.

rec_length = int(input("Enter the length of the Rectange : "))
rec_breadth = int(input("Enter the breadth of the Rectange : "))
rec_area = rec_length * rec_breadth
rec_parimeter = 2*(rec_length + rec_breadth)
print("The area of the Rectangle = {0}\nThe perimeter of the rectangle = {1}".format(rec_area,rec_parimeter))

circle_radius = int(input("Enter the radius of Circle : "))
circle_area =(22/7)*(circle_radius**2)
circle_circumference = 2*(22/7)*circle_radius
print("The area of the Circle = {0}\nThe circumference of the Circle = {1}".format(circle_area,circle_circumference))
