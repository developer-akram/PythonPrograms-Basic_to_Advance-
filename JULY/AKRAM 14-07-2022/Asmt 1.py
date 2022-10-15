# 1. WAP to divide even elements and odd elements separately in a tuple?

even_list = []
odd_list = []
a = (5,4,3,2,1,7,8,9,6)
print("Input Tuple :",a)
for i in a:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
else:
    print("Even numbers are :",even_list)
    print("Odd numbers are :",odd_list)