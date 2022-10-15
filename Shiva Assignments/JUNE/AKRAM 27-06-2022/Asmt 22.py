# 22. Write a program to calculate profit or loss.

cost_buy = int(input("Enter buying cost : "))
cost_sell = int(input("Enter selling cost : "))

if cost_sell - cost_buy > 0 :
    profit = cost_sell - cost_buy
    print("Profit is = ",profit)
else:
    loss = cost_buy - cost_sell
    print("Loss is = ",loss)