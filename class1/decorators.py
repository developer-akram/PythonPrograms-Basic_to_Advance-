# def fun1(value):
#     if value == 0:
#         return 1
#     if value == 1:
#         return 0
# fun2 = fun1(1)
# print(fun2)
def fn1(text):
    def fn2():
        print("This is first message")
        text()
        print("This is last message")
    return fn2


@fn1
def nameshow():
    print("My name is Khan")
# --------------------@fn1 can be written as also----------------------
# nameshoe = fn1(nameshow)
nameshoe()