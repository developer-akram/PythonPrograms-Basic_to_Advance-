# 6. Find the occurrence of an integer in the list

a = [12,54,23,76,12,23]
occur = int(input("Enter a number : "))
count = 0
for i in a:
    if i == occur:
        count += 1
print(occur,"Occurance :",count)
if occur not in a:
    print("Your input ia not available in the list")