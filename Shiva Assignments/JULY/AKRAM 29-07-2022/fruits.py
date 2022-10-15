
myshop = {"banana":[12,5],"apple":[10,10],"mango":[15,8]}
def displayshop():
    print("Available items are :")
    for i,j in myshop.items():
        print(f"[ {i} ] Quantity = {j[0]} cost/item = {j[1]}")

def purchases(f_name,quantity):
    for i,j in myshop.items():
        if i == f_name:
            if quantity > j[0]:
                print("Selected quantity is not available.Please drop some quantitieds.")
            else:
                print(f"You select [ {i} ] Quantity = {quantity}, total cost = {quantity} * {j[1]} = {quantity*j[1]}")
                j[0] -= quantity
                displayshop()

