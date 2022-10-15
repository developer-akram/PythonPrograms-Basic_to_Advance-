# 1. create a multi-dimension dictionary to store
# five student records and display max, min, total fees of students.

a = {1:{"name":"Akram","Fees":45000},2:{"name":"Ganesh","Fees":90000},3:{"name":"Rahul","Fees":75000}}
max_fees  = 0
sum = 0
for i in a:
    print("Name : {}\tFees : {}".format(a[i]["name"],a[i]["Fees"]))
    if a[i]["Fees"] > max_fees:
        max_fees = a[i]["Fees"]
min_fees = max_fees
for i in a:
    if a[i]["Fees"] < min_fees:
        min_fees = a[i]["Fees"]
    sum += a[i]["Fees"]
print("Maximum Fees :",max_fees)
print("Minimum Fees :",min_fees)
print("Sum of Fees : ",sum)