# Account creation and perform operations using functions

def account_create():
    global amount
    print("\tWelcome to Shiva bank\n\t\tAccount creation Form ")
    name = input("Enter full name : ")
    amount = int(input("Enter amount : "))
    ac_no = 112344321
    print("Congratulation...You account has been created successfully")
    print(
        f"Name : {name.upper()}\nAccount no : {ac_no}\nAccount Balance : {amount}\nISFC Code : {'SHIVA0123'}\nShiva Bank of India")


def check_bal(mycash):
    print("Your account balance is :", mycash)
    return mycash


def deposit_bal(dep, addcash):
    addcash += dep
    print(f"{dep} has been added sucessfully.\nCurrent balance : {addcash}")
    return addcash


def withdraw_bal(withcash, restbal):
    restbal -= withcash
    print(f"{withcash} has been withdrawn successfully.\nCurrent balance : {restbal}")
    return restbal


def options(account_cash):
    while True:
        print("[1] Withdraw\t\t[2] Deposit\n[3] Check Balance\t\t[4] Exit")
        choice = int(input("Enter your choice :"))
        if choice == 1:
            while True:
                withdraw = int(input("Enter the amount you want to withdraw : "))
                if withdraw > account_cash:
                    print("Sorry! Your withdraw balance is higher than your current balance")
                    continue
                else:
                    account_cash = withdraw_bal(withdraw, account_cash)
                    break
        elif choice == 2:
            add = int(input("Enter the amount to add : "))
            account_cash = deposit_bal(add, account_cash)
        elif choice == 3:
            account_cash = check_bal(account_cash)
        elif choice == 4:
            print("Account closed and deleted...\nNow going to exit...")
            break
        else:
            print("Invalid Choice...")
            continue


account_create()
options(amount)
