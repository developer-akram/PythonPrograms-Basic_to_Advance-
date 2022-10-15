mob = input("Enter mobile number : ")
max = 0
if mob.isnumeric() == True and len(mob) == 10:
    max = 0
    for i in mob:
        if i > max:
            max = i
    print(max)