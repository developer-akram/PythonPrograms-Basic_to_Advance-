# 2. WAP to convert a dictionary to set and set to the dictionary.

a = {"Sachin":"Cricketer","Messi":"Footballer","Arjit":"Singer","M J":"Dancer","Akram":"Gamer"}
b = set()
c = set()
print("Input Dictionary :\n[KEYS]\t [VALUES]")
for key, value in a.items():
    print(key,"\t",value)
    b.add(key)
    c.add(value)
print("\nConverting Dictionary to Set...\n")
print("[Keys of Dictionary]\nSet 1 :",b)
print("[Values of Dictionary]\nSet 2 :",c)
print("\nConverting Set to Dictionary...\n")
a.clear()
if len(b) == len(c):
    for i in range (len(b)):
        a[b.pop()] = c.pop()
print(a)