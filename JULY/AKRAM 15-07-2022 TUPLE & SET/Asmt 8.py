# 8. Counts the number of occurrences of item 50 from a tuple

a = (10,50,49,50,11,50,63,22,46,500,33,50.50,1,50)
print("Input tuple :\n",a)
count = 0
for i in a:
    if i == 50:
        count += 1
else:
    print("50 found in the tuple {} times".format(count))