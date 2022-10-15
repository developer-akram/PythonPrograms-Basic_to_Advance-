# 19. Write a program to input all sides of a triangle and check whether triangle is valid or not.

side_1 = int(input("Enter 1st side : "))
side_2 = int(input("Enter 2nd side : "))
side_3 = int(input("Enter 3rd side : "))

if side_1+side_2 > side_3 and side_2+side_3 > side_1 and side_1+side_3 > side_2 :
    print("Triangle is valid")
else:
    print("Triangle is not valid")