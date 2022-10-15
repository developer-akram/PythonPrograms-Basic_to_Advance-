# 4. Unpack the tuple into 4 variables
c_int = c_float = c_bool = c_str = 0
a = (10,49,"Star", True, 20, "Khan" ,14.45,56,False, "Akram")
print("User tuple :",a)
for i in a:
    if type(i) == str:
        c_str += 1
    elif type(i) == int:
        c_int += 1
    elif type(i) == float:
        c_float += 1
    elif type(i) == bool:
        c_bool += 1
    else:
        print("Unknown format")
print("There are \n[{}] string items\n[{}] integer items"
      "\n[{}] float items\n[{}] boolean items".format(c_str,c_int,c_float,c_bool))