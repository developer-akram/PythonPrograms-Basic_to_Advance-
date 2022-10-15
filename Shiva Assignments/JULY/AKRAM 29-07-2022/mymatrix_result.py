from mymatrix import matrix

choice = input("[a] for 2*2 matrix\n[b] for 3*3 Matrix\nPress a or b : ")
low = int(input("Enter minimum value of matrix elements : "))
high = int(input("Enter maximum value of matrix elements : "))
if choice == "a":
    matrix(2,low,high)
elif choice == "b":
    matrix(3,low,high)
else:
    print("Invalid choice...")