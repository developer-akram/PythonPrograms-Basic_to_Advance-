# 9. How to check if two strings are rotations of each other? (solution)

first = input("Enter first word : ")
second = input("Enter second word : ")
first = first * 2
if second in first:
    print("Strings are rotational of each other")
else:
    print("Strings are not rotational of each other")