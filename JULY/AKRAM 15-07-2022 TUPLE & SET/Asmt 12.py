# 11. WAP to reverse set elements
# (if random then display actual random and reverse of random elements)?

a = {10, 20, 30, 40, 50, 60}
print("Actual Elements  using set :",a)
b = []
for i in a:
    b.insert(0,i)
print("Reverse elements using set :",set(b))

