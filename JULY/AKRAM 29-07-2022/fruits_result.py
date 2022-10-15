
import fruits as test

test.displayshop()
while True:
    name = input("Type name of the item : ")
    numbers = int(input("Select Quantity : "))
    test.purchases(name,numbers)
    more = input("Type 'm' for more purchases or press any key to exit... : ")
    if more.lower() == "m":
        continue
    else:
        break