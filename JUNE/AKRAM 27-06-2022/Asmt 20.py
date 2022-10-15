# 20. Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

angle_1 = int(input("Enter 1st angle : "))
angle_2 = int(input("Enter 2nd angle : "))
angle_3 = int(input("Enter 3rd angle : "))

triangle = angle_1 + angle_2 + angle_3
if triangle == 180 :
    if angle_1 == angle_2 == angle_3:
        print("It's an Euilateral Triangle")
    else:
        if angle_1 == angle_2 or angle_2 == angle_3 or angle_1 == angle_3:
            print("It's an Isosceles Triangle")
        else:
            if angle_1 != angle_2 != angle_3:
                print("It's an Scalene Triangle")
else:
    print("Triangle is not valid.Please try again...")