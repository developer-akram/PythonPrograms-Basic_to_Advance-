# 21. W a p to print table of input digit except if input is 7 display the first 7 multiples of 7

num = int(input("Enter a number: "))
i = 1
while i <= 10 :
    print("{0} * {1} = {2}".format(num,i,num*i))
    if num == 7 and i ==7:
        break
    i += 1