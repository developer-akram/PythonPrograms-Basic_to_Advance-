# 3. Write a program to display the subject marks of the student which will be entered by
# the user. if the entered subject mark is eligable for grace then display marks
# including grace marks otherwise actual marks will display.

mark = int(input("Enter mark : "))
if mark >= 28 and mark < 33 :
    mark_g = 33 - mark
    print("Grace mark = ",mark_g)
    mark += mark_g
print("Updated mark = ",mark)