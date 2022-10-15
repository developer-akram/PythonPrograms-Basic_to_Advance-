# 1. Write a program to reverse dictionary elements

a = {"Rahul":"Hero","Manish":(22,23),"Kiran":[333,334],"Arjun":{4444,"Pro"},"Akram":55555}

key = []
value = []
count = 0
print("Given Dictionary :")
for i, j in a.items():
    count += 1
    print("Key {} : {}\t\tValue {} : {}".format(count,i,count,j))
    key.append(i)
    value.append(j)
print("Reverse Dictionary :")
count = 0
if len(key) == len(value):
    for i in range(len(key)-1,-1,-1):
        count += 1
        print("Key {} : {}\t\tValue {} : {}".format(count, key[i], count, value[i]))
