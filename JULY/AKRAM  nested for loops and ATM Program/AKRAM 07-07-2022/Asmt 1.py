account = 10000.00
pin = 8520
print("Welcome to AKRAM ATM")
count = 3
while True:
    pin_input = int(input("Enter four digit ATM pin : "))
    if pin_input != pin :
        if count > 0:
            print("You have entered wrong PIN.{} chances left".format(count))
            count = count - 1
            continue
        else:
            print("You entered wrong PIN more than 3 times.Please try again after 24 hours.")
            break
    else:
        while True:
            print("[1] Check Balance\n[2] Deposit Money\n[3] Withdraw Money\n[4] Change ATM pin\n[5] Exit")
            choice = int(input("Enter your choice : "))
            if choice == 1:
                print("Your Total Account Balance = %.2f INR"%account)
                back_exit = input("Enter b to back in Menu or enter any key to exit! Enter : ")
                if back_exit == "b":
                    continue
                else:
                    break
            elif choice == 2:
                deposit = float(input("Enter total amount you want to deposit : "))
                account = account + deposit
                print("Your updated Acoount Balance is : %.2f INR"%account)
                back_exit = input("Do u want to perform more operation? Type 'y' to yes or enter any key to exit. Enter : ")
                if back_exit == "y":
                    continue
                else:
                    break
            elif choice == 3:
                while True:
                    withdraw = float(input("Enter the cash amount you want to withdraw : "))
                    if withdraw > account :
                        print("Your withdraw amount is greater than your account balance. Please enter amount below %.2f INR"%account)
                        continue
                    else:
                        account = account - withdraw
                        print("You have succesfully withdawl %.2f INR"%withdraw)
                        print("Your account balance %.2f INR"%account)
                        back_exit = input("Do u want to perform more operation? Type 'y' to yes or enter any key to exit. Enter : ")
                        break
                if back_exit == "y":
                    continue
                else:
                    break
            elif choice == 4:
                print("[[[ PIN CHANGE SERVICE]]]")
                while True :
                    update_pin = int(input("Enter the new pin : "))
                    update_pin_2 = int(input("Re-Enter new pin to confirm : "))
                    if update_pin != update_pin_2 or pin == update_pin or update_pin_2 == pin:
                        print("Your new pin and re-enter new pin should be equal and Old pin cannot be same as pin pin")
                        continue
                    else:
                        print("PIN changed successfully.\nOld pin = [{}],".format(pin),end=" ")
                        pin = update_pin
                        print("New pin = [{}]\nNow Re-Login to Continue...".format(pin))
                        break
            elif choice == 5:
                print("Going to Exit...")
                break
            else:
                print("Invalid Option ,Please try again...")
                continue
            break