# 2. WAP to count total even number and Odd number in Tuple?

a = (5,4,3,2,1,7,8,9,11,6)
count_even = 0
count_odd = 0
print("Input tuple :",a)
for i in a:
    if i % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
else:
    print("Total even numbers :",count_even)
    print("Total odd numbers :",count_odd)