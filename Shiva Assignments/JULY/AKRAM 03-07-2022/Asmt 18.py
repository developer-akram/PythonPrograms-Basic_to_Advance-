# 18. Write a program to print all prime numbers  that fall between two numbers including both(accept two numbers from the user)

min_num = int(input("Enter starting range : "))
max_num = int(input("Enter target range : "))
if min_num > max_num:
    min_num, max_num = max_num, min_num
print("Prime numbers are :",end=" ")
for i in range (min_num,max_num+1):
    for j in range (2,min_num):
            if min_num % j == 0:
                break
    else:
        print(min_num,end=" ")
    min_num += 1