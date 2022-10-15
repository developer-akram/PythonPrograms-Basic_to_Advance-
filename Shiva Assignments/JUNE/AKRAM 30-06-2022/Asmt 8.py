# 8. Write a   program to check whether a number is palindrome or not.

num = int(input("Enter any number : "))
save = num
pldm = 0
while num > 0 and num !=0 :
    reminder = num % 10
    pldm =pldm * 10 + reminder
    num //= 10
if save == pldm :
    print(save,"is a Palindrome number")
else:
    print(save,"is not a Palindrome number")