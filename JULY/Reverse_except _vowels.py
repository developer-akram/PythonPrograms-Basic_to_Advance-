# Wap to reverse string except vowels and the position of vowels are should be same

text = input("Enter any text or sentence : ")
mylist = text.split(" ")
anslist = []
for one in mylist:
    a = list(one)
    vowels = ("e","i","o","u","a")
    r = []
    x = []
    pos = []
    elements = ""
    for i in range (len(a)):
        if a[i].lower() in vowels:
            pos.append(i)
            r.append(a[i])
        else:
            x.insert(0,a[i])
    for i in range (len(r)):
        x.insert(pos[i],r[i])
    for k in x:
        elements += k
    anslist.append(elements)
print(f"Input : {text}")
print("Output : ",end="")
for i in anslist:
    print(i,end=" ")
print("\nOutput in reverese : ",end="")
for i in range (len(anslist)-1,-1,-1):
    print(anslist[i],end=" ")



