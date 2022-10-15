#--------------------------------------------ASSIGNMENT 12----------------------------------------------
# Write a   program to enter distance of a city in km convert it into meter and feet and inches.

city_distance = int(input("Enter the distance between two Cities in KMs : "))

print("Distance between two cities in KMs : ",city_distance,"kms")
print("Distance between two cities in Mtrs : ",city_distance*1000,"meters")
print("Distance between two cities in Feets : ",city_distance*3280,"feets")
print("Distance between two cities in Inchs : ",city_distance*39370.079,"cms")