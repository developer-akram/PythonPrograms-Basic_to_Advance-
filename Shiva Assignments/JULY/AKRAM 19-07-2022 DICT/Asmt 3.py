# 3. Write a program to find maximum element in dictionary

a = {"Vrushank":45.78,"Mukesh":23,"Ganesh":53.97,"Neha":15,"Akram":22,"King":"Queen"}
print("Input Dictionary :\n{}\n".format(a))
max = 0
print("Value pairs are :")
for item in a:
    if type(a[item]) == int or type(a[item]) == float:
        print(a[item], end="\t\t")
        if a[item] > max:
            max = a[item]
    else:
        print("\n\n"+str(a[item]),"is not a number type.So, it has been removed")
print("Maximum Element in above dictionary :",max)