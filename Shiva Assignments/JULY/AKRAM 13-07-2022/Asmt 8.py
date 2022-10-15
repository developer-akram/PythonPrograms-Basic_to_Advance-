# 8. Count Pairs with given sum

a = [1,2,3,5,6,4]
sum = int(input("Enter sum value : "))
for i in range (len(a)):
    for j in range (1,len(a)):
        if a[i] + a[j] == sum:
            print("Count pairs Found : {} and {}".format(a[i],a[j]),end=" || ")
            print("Calculation Form : {} + {} = {}".format(a[i],a[j],sum))
