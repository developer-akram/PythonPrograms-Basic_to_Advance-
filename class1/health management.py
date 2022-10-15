name = {1 : "Harry", 2 : "Rohan", 3 : "Hammad"}
data = {1 : "Diet", 2: "Excercise"}
io = {1 : "Log", 2 : "Retrive"}

def gettime():
    import datetime
    return datetime.datetime.now()
try :
    for key, value in name.items():
        print("Choose",key,"for",value)
    print("Enter Your Choice : ")
    s_name = int(input())
    print("Selected name is : ",name[s_name])
    for key, value in data.items():
        print("",key,"for",value)
    print("Select an Option :")
    s_data = int(input())
    print("You Choose ",data[s_data],"of",name[s_name])
    for key, value in io.items():
        print("",key,"for",value)
    print("Select an Option :")
    s_io = int(input())
    print("You want to",io[s_io],data[s_data],"of",name[s_name])
    if s_io == 1 :
        with open(name[s_name]+"_"+data[s_data]+".txt","a") as f :
            k = "y"
            while k == "y":
                print("Enter the",data[s_data])
                w_data = input()
                f.write("["+str(gettime())+"]:"+w_data+"\n")
                print(data[s_data],"records save successfully for",name[s_name])
                k = input("Do you log more? y/n")
                if k == "y":
                    continue
                elif k == "n":
                    print("going to Exit...")
                else:
                    print("Invalid Choice.Exit...")
    if s_io == 2:
        with open(name[s_name]+"_"+data[s_data]+".txt") as f :
            a = f.readlines()
            for line in a :
                print(line, end="e")
except Exception as e :
    print("Try Again")