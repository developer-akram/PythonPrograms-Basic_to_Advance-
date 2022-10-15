# -----------------------------------------FAULTY CALCULATOR------------------------------

print("Welcome to the Calculator")
print("type [+] for addition ")
print("type [-] for substration ")
print("type [*] for multipication ")
print("type [/] for division ")
print("type [**] for power ")
print("type [%] for module ")
user_opertaion = str(input("Enter an opertion you want to perform : "))
first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number : "))
if user_opertaion == "+":
    if first_number == 56 and second_number == 9:
        print("56 + 9 = 77")
    else :
        print(first_number,user_opertaion,second_number,"=",first_number + second_number )
elif user_opertaion == "*":
    if first_number == 45 and second_number == 3:
        print("45 * 3 = 555")
    else :
        print(first_number,user_opertaion,second_number,"=",first_number * second_number )
elif user_opertaion == "/" :
    if first_number == 56 and second_number == 6:
        print("56 / 6 = 4")
    else :
        print(first_number,user_opertaion,second_number,"=",first_number / second_number )
elif user_opertaion == "-" :
    print(first_number, user_opertaion, second_number, "=", first_number - second_number)
elif user_opertaion == "**" :
    print(first_number, user_opertaion, second_number, "=", first_number ** second_number)
elif user_opertaion == "%" :
    print(first_number, user_opertaion, second_number, "=", first_number % second_number)
else :
    print("You choose an invalid option.")