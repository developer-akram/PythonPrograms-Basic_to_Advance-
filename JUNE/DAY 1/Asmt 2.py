#---------------------------------------ASSIGNMENT 2---------------------------------------------
# The distance between two cities (in km.) is input through the keyboard.
# Write a program to convert and print this distance in meters, feet, inches and centimeters.

city_distance = int(input("Enter the distance between two Cities : "))
distance_mtr = city_distance*1000
distance_feet = city_distance*3280
distance_inch = city_distance*39370.079
distance_cms =  city_distance*100000
print("Distance between two cities in KMs : ",city_distance,"kms")
print("Distance between two cities in Mtrs : ",distance_mtr,"mtrs")
print("Distance between two cities in Feets : ",distance_feet,"feets")
print("Distance between two cities in Inchs : ",distance_inch,"inchs")
print("Distance between two cities in CMs : ",distance_cms,"cms")