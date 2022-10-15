a = "Akram"
b = 4
#c = "This is %s %s"%(a, b)
c = "This is {1} {0}"
x = c.format(a, b)
print(x)
d = f"Khanstar {a} {b}{5*4}"
print(d)