# 18. WAP to calculate square and cube of one digit positive number?

num = int(input("Enter a number : "))
if num > 0 and num <= 9:
    while True:
        print("Square of {0} = {1}".format(num,num**2))
        print("Cube of {0} = {1}".format(num, num**3))
        break
else:
    print("Your input should be one digit positive number.")