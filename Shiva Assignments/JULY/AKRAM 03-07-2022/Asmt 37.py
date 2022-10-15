# 37. Write a python program to print all prime numbers between 0 to 100 ,
# and print how many prime numbers are there.

print("Prime numbers are :",end=" ")
count = 0
for i in range (1,100+1):
    for j in range (2,i):
            if i % j == 0:
                break
    else:
        count = count + 1
        print(i,end=" ")
print("\nTotal number of prime numbers =",count)