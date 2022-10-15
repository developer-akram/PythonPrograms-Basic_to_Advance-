# 10. Exercise 7: Modify the tuple

a = ('5','4','3','2','1','7','8','9','6')
while(True):
    print("\n\nDefault tuple :",tuple(a))
    print("Welcome to Tuple Modification System :")
    print("[1] Delete items \n[2] Add items \n[3] Change item \n[4] Delete entire tuple"
          "\n[5] Sort ascending order \n[6] Sort descending order\n[7] Exit")
    choice = int(input("Enter your choice : "))
    a = list(a)
    if choice == 1:
        while True:
            del_item = input("Enter the item you want to delete : ")
            if del_item in a:
                a.remove(del_item)
                print(del_item,"is deleted")
                print("Updated Tuple :",tuple(a))
                x = input("Type 'm' to delete more items or press any key to exit : ")
                if x == "m":
                    continue
                else:
                    break
    elif choice == 2:
        while True:
            add = input("Enter the item you want to add : ")
            print("In which position you want to add ?\n[1] Last position \n[2] Custom position")
            pos = int(input("Enter your choice : "))
            if pos == 1:
                a.append(add)
            elif pos == 2:
                c_pos = int(input("In which position you want to add : "))
                a.insert(c_pos-1,add)
            else:
                print("Invalid Choice")
            print("Updated Tuple :", tuple(a))
            x = input("Type 'm' to delete more items or press any key to exit : ")
            if x == "m":
                continue
            else:
                break
    elif choice == 3:
        while True:
            print(tuple(a))
            c_value = input("Select only one value from the tuple : ")
            if c_value in a :
                up_value = input("Enter your modified value : ")
                for i in range (len(a)):
                    if a[i] == c_value:
                        a[i] = up_value
                        print("Previous value : {}\nUpdated value : {}".format(c_value,up_value))
                        print("Updated Tuple :", tuple(a))
                        break
                x = input("Type 'm' to delete more items or press any key to exit : ")
                if x == "m":
                    continue
                else:
                    break
            else:
                print("Selected value is not present in the tuple.Try again...")
                continue
    elif choice == 4:
        a = tuple(a)
        x = input("Do you really want to delete entire tuple? type 'y' for yes or press any to cancel : ")
        if x == "y":
            del a
            print("Entire tuple deleted successfully.")
            print("Now exit automatically")
            break
        else:
            print("Your tuple is safe,Going to main screen...")
    elif choice == 5:
        for i in range(len(a)):
            a[i] = int(a[i])
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                if a[i] > a[j]:
                    a[i],a[j] = a[j],a[i]
        print("Tuple in ascending order :",tuple(a))
        x = input("Type 'm' for main menu or press any key to exit : ")
        if x == "m":
            for i in range(len(a)):
                a[i] = str(a[i])
            continue
        else:
            print("Going to exit...")
            break
    elif choice == 6:
        for i in range(len(a)):
            a[i] = int(a[i])
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                if a[i] < a[j]:
                    a[i],a[j] = a[j],a[i]
        print("Tuple in descending order :",tuple(a))
        x = input("Type 'm' for main menu or press any key to exit : ")
        if x == "m":
            for i in range(len(a)):
                a[i] = str(a[i])
            continue
        else:
            print("Going to exit...")
            break
    elif choice == 7:
        print("You choose exit..by bye")
        break
