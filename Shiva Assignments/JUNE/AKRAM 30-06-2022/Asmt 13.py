# 13. Write a  program to find all factors of a number.

num = int(input("Enter any number : "))
i = 1
count = ""
while i <= num :
    if num % i == 0 :
        if i == num :
            count = count + str(i)
        else:
            count = count + str(i) + " , "
    i += 1
print("factors of {0} = {1}".format(num,count))