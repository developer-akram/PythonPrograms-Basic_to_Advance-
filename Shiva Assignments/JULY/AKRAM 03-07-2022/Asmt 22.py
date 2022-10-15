# 22. Write a program that keep on accepting number from the user until user enters Zero.
# Display the sum and average of all the numbers.

sum = 0
show_sum = ""
while True:
    number = int(input("Enter number : "))
    sum = sum + number
    if number == 0:
        print("{}0 = {}".format(show_sum,sum))
        break
    show_sum = show_sum + str(number) + " + "