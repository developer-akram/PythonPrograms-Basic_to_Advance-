# 3. WAP to convert a dictionary to list and list to the dictionary.

a = {"Akram ":90, "Vrushank":80, "Mukesh":100,"Ganesh":40}
b = []
c = {}
print("Given Dictionary :",a)
for i, j in a.items():
    b.append(i)
    b.append(j)
print("Dictionary to List :",b)
for i in range (0,len(b),2):
    c[b[i]] = b[i+1]
print("List to Dictionary :",c)