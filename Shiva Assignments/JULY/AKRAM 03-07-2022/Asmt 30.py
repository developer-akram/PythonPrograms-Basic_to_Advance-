# 30. Write a python program to find the sum of all even numbers from 1 to 10
sum_e = 0
show_e = ""
for i in range (1,11):
    if i % 2 == 0:
        if i == 10:
            show_e = show_e + str(i) + " ="
        else:
            show_e = show_e + str(i) + " + "
        sum_e += i
print("Sum of even numbers:\n"+show_e,sum_e)