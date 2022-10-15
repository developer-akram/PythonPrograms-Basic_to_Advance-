# 1. Find the Kth largest and Kth smallest number in an array

a = [12,4,63,76,22,57,82,1,4,77,22,66,22,56,44,82,57]
b = []
print(f"Given array :\n{a}")
for i in a:
    if i not in b :
        b.append(i)
b.sort()
choice = int(input("Enter the nth range : "))
if choice > len(b):
    print("Sorry...Total array size is lesser than your position.")
else:
    sub_c = int(input("[1] for smallest\n[2] for hightest\nEnter your choice : "))
    if sub_c == 1:
        print(f"Lowest position {choice} number : [{b[choice-1]}]")
    elif sub_c == 2:
        b_neg = b[::-1]
        print(f"Heighest position {choice} number : [{b[choice - 1]}]")
    else:
        print("Invalid choice....")