#-----------------------------------------ASSIGNMENT 10--------------------------------------------------
#Q. If the total selling price of 15 items and the total profit earned
# on them is input through the keyboard, write a program to
# find the cost price of one item.

sell_price = int(input("Enter the total selling price of the 15 items : "))
profit = int(input("Enter the total profit earned on 15 items : "))

total_buying_price = sell_price - profit
each_item_buy_price = total_buying_price / 15

print("The buying cost of one item is : ",each_item_buy_price)