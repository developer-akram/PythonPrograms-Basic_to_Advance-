print("Welcome to Driving School")
age = int(input("Enter your Age : "))
if age>18 and age<100:
    print("Congrats, Yon can drive.")
elif age<18 and age>6 :
    print("Sorry, You cannot drive.")
elif age == 18:
    print("Your age is 18. We will let you know once you become eligible")
else :
    print("You entered invalid age.")