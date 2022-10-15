# 3. WAP to print 1 to 5 and  5 to 1 using a single while loop?

range = int(input("Enter a range : "))
i = 1
while i <= range :
    print(i)
    i += 1
    if i == range+1:
        def loop(i):
            if i > 0:
                print(i)
                loop(i-1)
        loop(i-1)
