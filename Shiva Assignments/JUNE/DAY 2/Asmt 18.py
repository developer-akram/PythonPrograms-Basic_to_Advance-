#---------------------------------------------ASSIGNMENT 18--------------------------------------------
# 18.Write a   program to enter two angles of a triangle and find the third angle.

angle_first = int(input("Enter the first angle of the triangle : "))
angle_second = int(input("Enter the second angle of the triangle : "))
angle_third = 180 - (angle_first + angle_second)
print("Total angle of a triangle = 180°")
print("First angle is = {0}°\nSecond angle is = {1}°\nThird angle is = {2}°".format(angle_first,angle_second,angle_third))