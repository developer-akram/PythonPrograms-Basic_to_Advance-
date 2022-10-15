mob = int(input("Enter mobile number : "))
if len(str(mob)) == 10:
    max = 0
    def maxo(mob,max_1=0,max_2=0):
        max = 0
        while mob != 0:
            r = mob % 10
            mob = mob // 10
            if r > max and r != max_1 and r != max_2:
                max = r
        return max
    f_max = maxo(mob)
    print("First Max =",f_max)
    s_max = maxo(mob,f_max)
    print("Second Max =",s_max)
    t_max = maxo(mob,f_max,s_max)
    print("Third Max =",t_max)
else:
    print("Mobile number should be 10 digits")
