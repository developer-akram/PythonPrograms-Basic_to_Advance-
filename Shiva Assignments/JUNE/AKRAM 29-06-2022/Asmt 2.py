# 2. WAP to print a table of any entered number?

num = int(input("Enter a number: "))
i = 1
while i <= 10 :
    # print(str(num)+" * "+str(i)+" = "+str(num*i))
    #or using .FORMAT
    print("{0} * {1} = {2}".format(num,i,num*i))
    # or using F-STRING
    # print(f"{num} * {i} = {num * i}")
    i += 1