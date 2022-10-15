# 6. WAP to display "YES" and "NO" when the user press 'y' and 'n'?

user_input = input("Enter 'y' or 'n' : ")
user_input = user_input.lower()
if user_input == "y" :
    print("YES")
elif user_input == "n" :
    print("NO")
else:
    print("Wrong Input.Please try again...")