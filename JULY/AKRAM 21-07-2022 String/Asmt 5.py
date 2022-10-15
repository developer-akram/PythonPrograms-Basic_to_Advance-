# 5. WAP to display a number of repeated char in String?

name = input("Enter any name : ")
for i in range (len(name)):
    if name[i] in name[:i]:
        continue
    count = 1
    for j in range(i+1,len(name)):
        if name[i] == name[j]:
            count +=1
    else:
        print("Count of {} = {}".format(name[i],count))
