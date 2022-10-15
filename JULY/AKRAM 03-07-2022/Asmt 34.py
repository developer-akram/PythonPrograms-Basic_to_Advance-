# 34. Write a python program to read four numbers (representing the four octets of an IP) and
# print the next five IP address
# Input:
# 192 168 255 252
# ----------Output---------
# 192 168 255 253
# 192 168 255 254
# 192 168 255 255
# 192 169 0 0
# 192 169 0 1

num_1 = int(input("Enter number 1 : "))
num_2 = int(input("Enter number 2 : "))
num_3 = int(input("Enter number 3 : "))
num_4 = int(input("Enter number 4 : "))
print("Input : \n{} {} {} {}".format(num_1,num_2,num_3,num_4))
print("Output : ")
for i in range (1,3):
    if i == 1:
        for j in  range(1,4):
            print("{} {} {} {}".format(num_1,num_2,num_3,num_4+j))
    num_3=0
    num_4 =0
    print("{} {} {} {}".format(num_1,num_2+1,num_3,num_4+(i-1)))
