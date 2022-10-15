# 28. Write a function to display prime numbers below any number accepted from the user.

num = int(input("Enter a range : "))

for i in range (1, num):
    for j in range (2,i):
        if i % j == 0:
            break
    else:
        print(i,end=" ")