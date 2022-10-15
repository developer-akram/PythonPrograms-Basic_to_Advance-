# 4. Write a program to find key in dictionary

a = {45:"Mukesh",93.21:"Akram",57:"Ganesh",155:"Neha",10.22:"Vrushank","King":"Queen"}
print("Input Dictionary :\n{}\n".format(a))
max = 0
print("Key elements are :")
for key in a:
    if type(key) == int or type(key) == float:
        print(key,end="\t\t")
        if key > max:
            max = key
    else:
        print("\n\n"+str(key),"is not a number type.So, it has been removed")
print("Maximum Element in above dictionary :",max)