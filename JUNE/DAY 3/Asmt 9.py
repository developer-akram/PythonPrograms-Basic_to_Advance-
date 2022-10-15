#-----------------------------------------ASSIGNMENT 9--------------------------------------------------
# Q. A cashier has currency notes of denominations 10, 50 and
# 100. If the amount to be withdrawn is input through the
# keyboard in hundreds, find the total number of currency notes
# of each denomination the cashier will have to give to the withdrawer.

user_input = int(input("Enter the cash amount you want to withdraw multiple of 100: "))

notes_100 = user_input//100
notes_50 = user_input//50
notes_20 = user_input//20

print("Either \nyou will get 100/- notes {0} times or \n"
      "you will get 50/- notes {1} times or \n"
      "you will get 20/- notes {2} times.".format(notes_100,notes_50,notes_20))

