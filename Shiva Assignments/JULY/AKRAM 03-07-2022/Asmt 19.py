# 19. Write a program to display sum of odd numbers and even numbers that fall between 12 and 37(including both numbers)
sum_e = sum_o = 0
show_e = show_o = ""
for i in range (12,38):
    if i % 2 == 0:
        if i == 36:
            show_e = show_e + str(i) + " = "
        else:
            show_e = show_e + str(i) + " + "
        sum_e += i
    else:
        if i == 37:
            show_o = show_o + str(i) + " = "
        else:
            show_o = show_o + str(i) + " + "
        sum_o += i
print("Sum of even numbers:\n"+show_e,sum_e)
print("Sum of even numbers:\n"+show_o,sum_o)