# 15. Write a   program to swap first and last digits of a number.


num = int(input("Enter a number : "))
num =str(num)
while(True):
    first = num[0]
    length = len(num)
    middle = num[1:length -1]
    last = num[-1]
    result = last+middle+first
    result = int(result)
    break
print("Reverse first and last digit output = ",result)
