# 10. Write a   program to find frequency of each digit in a given integer.

num = int(input("Enter a number :"))
i = 1
new = num
while True:
    if i < 10 :
        count = 0
        while num > 0 :
            r = num % 10
            if i == r :
                count += 1
            num //= 10
        print("Frequency of {0} = {1}".format(i,count))
        num = new
        i +=1
