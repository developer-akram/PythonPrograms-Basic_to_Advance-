#5. Write a   program to print all natural numbers in reverse (from n to 1).

num = int(input("Enter a range of natural number to show in reverse: "))
while num > 0 :
    print(num, end=" ")
    num -=1