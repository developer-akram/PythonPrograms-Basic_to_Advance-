#3. WAP to print a table of odd numbers?

num = int(input("Enter a number : "))
if num % 2 != 0:
    for i in range (1, 11):
        print("{} * {} = {}".format(num,i,num*i))
else:
    print("Enter only odd values.")