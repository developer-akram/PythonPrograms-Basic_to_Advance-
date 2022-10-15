# 21.Write a program to enter or append n numbers in a list.

list1 = []
add = int(input("How many numbers you want to add in this list : "))
for i in range (add):
    a = input("Enter no {} value : ".format(i+1))
    list1.append(a)
print("Your list :\n",list1)