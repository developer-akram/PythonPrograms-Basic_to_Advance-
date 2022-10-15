#2. Write a program to find greatest number amoung three numbers (USING ELIF)

num_1 = int(input("Enter 1st number : "))
num_2 = int(input("Enter 2nd number : "))
num_3 = int(input("Enter 3rd number : "))

if num_1 > num_2 and num_1 > num_3 :
    print("1st number is Greatest.")
elif num_2 > num_3 :
    print("2nd number is greatest.")
else:
    print("3rd number is greatest.")