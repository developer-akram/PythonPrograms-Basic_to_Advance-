#-----------------------------------------ASSIGNMENT 14-----------------------------------------
# Write a  program to enter temperature in Fahrenheit and convert to Celsius

temp_in_f = int(input("Enter the temperature in Farenheit degree : "))
temp_in_c = float((temp_in_f-32)*(5/9))
print("The temperature in Centigrade Degree : ",temp_in_c)