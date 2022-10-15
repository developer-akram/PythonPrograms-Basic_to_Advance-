# 2. Write a program to reverse dictionary elements
# and showing output in dictionary format

a = {"Rahul":"Hero","Manish":(22,23),"Kiran":[333,334],"Arjun":{4444,"Pro"},"Akram":55555}
b = {}
key = []
value = []
print("Given Dictionary :\n",a)
for i, j in a.items():
    key.append(i)
    value.append(j)
if len(key) == len(value):
    for i in range(len(key)-1,-1,-1):
        b.update({key[i]:value[i]})
print("Reverse Dictionary :\n",b)