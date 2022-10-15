# ----------------------------------------ASSIGNMENT 13---------------------------------------
#Q. WAP to evaluate the middle number in three-digit numbers based on order?

user_input = int(input("Enter any three digit number : "))
first = user_input % 10
user_input = user_input // 10
second = user_input % 10
user_input = user_input // 10
third = user_input % 10

if first > second and first < third or first < second and first > third:
    print("Middle number is : ",first)
elif second > first and second < third or second < first and second > third:
    print("Middle number is : ",second)
elif third > first and third < second or third < first and third > second:
    print("Middle number is : ",third)
else:
    print("Middle number is not possible with this number.")