#----------------------------------------ASSIGNMENT 21--------------------------------------------
# 21.Write a program to enter marks of five subjects and calculate total, average and percentage.

user_sub1 = int(input("Enter the marks of 1st subject out of 100 : "))
user_sub2 = int(input("Enter the marks of 2nd subject out of 100 : "))
user_sub3 = int(input("Enter the marks of 3rd subject out of 100 : "))
user_sub4 = int(input("Enter the marks of 4th subject out of 100 : "))
user_sub5 = int(input("Enter the marks of 5th subject out of 100 : "))

user_total = (user_sub1 + user_sub2 + user_sub3 + user_sub4 + user_sub5)
user_average = (user_total / 5)
user_percentage = (user_total /5)

print("Total of five Subjects  = {0}\nThe average of five Subjects = {1}"
      "\nPercentage of five Subjects = {2}%".format(user_total,user_average,user_percentage))