# 17. Accept 10 numbers from the user and display their average.

s = ""
sum = 0
for i in range (1,11):
    a = int(input("Enter number {} : ".format(i)))
    sum = sum + a
    if i == 10:
        s = s + str(a) + " "
    else:
        s = s + str(a) + " + "
print("({}) / 2 = {}".format(s,sum / 10))

# num_1 = int(input("Enter number 1 : "))
# num_2 = int(input("Enter number 2 : "))
# num_3 = int(input("Enter number 3 : "))
# num_4 = int(input("Enter number 4 : "))
# num_5 = int(input("Enter number 5 : "))
# num_6 = int(input("Enter number 6 : "))
# num_7 = int(input("Enter number 7 : "))
# num_8 = int(input("Enter number 8 : "))
# num_9 = int(input("Enter number 9 : "))
# num_10 = int(input("Enter number 10 : "))
#
# avg = (num_1 + num_2 + num_3 + num_4 + num_5 + num_6 + num_7 + num_8 + num_9 + num_10) / 10
# print("({}+{}+{}+{}+{}+{}+{}+{}+{}+{})/2 = {}".format(num_1,num_2,num_3,num_4,num_5,num_6,num_7,num_8,num_9,num_10,avg))
