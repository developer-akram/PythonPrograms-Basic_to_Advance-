# 7. Sort a tuple of tuples by 2nd item

a = (("Ganesh",12),("Vrushank",9),("Neha",22),("Mukesh",11),("Akram",5))
print("Input Tuple :\n",a)
a = list(a)
for i in range (len(a)):
    for j in range (i+1,len(a)):
        if a[i][1] > a[j][1]:
            a[i],a[j] = a[j],a[i]
print("Tuple Sorted by 2nd item :\n",tuple(a))
