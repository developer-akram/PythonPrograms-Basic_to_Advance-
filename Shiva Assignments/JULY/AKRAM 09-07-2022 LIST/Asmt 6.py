# 6. How to take input from Users in LIST?

list1 = []
num = int(input("How many values you want to input : "))
for i in range (num):
    a = input("Enter no {} : ".format(i+1))
    list1.append(a)
print("Your list =",list1)