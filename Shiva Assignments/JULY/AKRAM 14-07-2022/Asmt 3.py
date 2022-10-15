# 3. WAP to count total integer, float, and string in a tuple?

a = ((1,'List',2,'is',3,'a',4,45.66,'compound',5,'data type', 87.33,6,'in', 7,'Python',4,66))
count_int = 0
count_float = 0
count_string = 0
for i in a:
    if type(i) == int:
        count_int += 1
    elif type(i) == str:
        count_string += 1
    elif type(i) == float:
        count_float += 1
    else:
        print("Unknown type.")
else:
    print("Total Numbers :",count_int)
    print("Total Strings :",count_string)
    print("Total Float Numbers :",count_float)