# -----------------------------------------H ASSIGNMENT 4---------------------------------------
# 4 WAP to calculate the area of a triangle, circle, and rectangle in the same program where the value of pi,
# the base of the triangle, and the height of the rectangle will be constant.

pi = (22/7)

base_tangle = 5
print("--------------TRIANGLE----------------")
print("Base of the triangle = ",base_tangle)
height_tangle = int(input("Just input the height of the triangle : "))
area_tangle = (base_tangle * height_tangle) / 2
print("Area of the triangle = ",area_tangle)

height_rangle = 8
print("--------------RECTANGLE----------------")
print("Height/Width of the rectangle = ",height_rangle)
length_rangle = int(input("Just input the length of the rectangle : "))
area_rangle = height_rangle * length_rangle
print("Area of the rectangle = ",area_rangle)

print("--------------CIRLE----------------")
radius_circle = int(input("Enter the radius of the circle : "))
area_circle = pi * (radius_circle**2)
print("Area of the cirle = ",area_circle)




