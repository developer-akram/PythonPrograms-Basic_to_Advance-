#-----------------------------------------------ASSIGNMENT 4----------------------------------------
# Temperature of a city in Fahrenheit degrees is input through the keyboard.
# Write a program to convert this temperature into Centigrade degrees.

temp_in_f = int(input("Enter the temperature in Farenheit degree : "))
temp_in_c = float((temp_in_f-32)*(5/9))
print("The temperature in Centigrade Degree : ",temp_in_c)
