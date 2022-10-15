try :
    a = int(input("How many rows you want to print : "))
    value = "*"
    boolean = int(input("Choose one\n[1] for TRUE\n[0] for FALSE\nEnter your input : "))
    while(a>0) :
        if boolean == 1:
            print(value)
            value+="*"
            a-=1
        elif boolean == 0:
            print(value*a)
            a-=1
        else :
            print("Invalid Input.")
except Exception as e :
    print("Invalid Input.")