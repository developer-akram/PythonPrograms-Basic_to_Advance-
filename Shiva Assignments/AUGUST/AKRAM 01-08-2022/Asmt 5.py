# 5. Find the missing integer from array
import random
a = input("Enter the numbers like 1 2 3:")
a = a.split(" ")
a = list(map(int,a))
b = a.copy()
print("Given list :",a)

def removeitem():
    a.remove(key)
    print("Array after removing one element :", a)
    for i in b:
        if i not in a:
            print(f"Deleted item : [{i}]")

choice = input("Do u want to remove element manually ? if yes type 'y' else press any key : ")
if choice == "y":
    key = int(input("Enter the element you want to remove : "))
    removeitem()
else:
    key = random.choice(a)
    removeitem()