#------------------------------------------------ASSIGNMENT 19--------------------------------------
# 19.Write a   program to enter base and height of a triangle and find its area.

input_base = int(input("Enter the base of triangle : "))
input_height = int(input("Enter the height of triangle : "))

area  = (input_base * input_height) / 2
print("Base = {0} , Height = {1} ,Area is = {2}".format(input_base,input_height,area))
