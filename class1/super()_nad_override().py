# class A:
#     var3 = "I am main variable of Class A"
#     def __init__(self):
#         self.var2 = "I am the first other name instance variable of Class A"
#         # self.var3 = "I am the first same name instance variable of Class A"
# class B(A):
#     # var3 = "I am the main variable of Class B"
#     pass
#
# a = A()
# b = B()
#
# print(b.var3)

class A :
    var1 = "Main Class"
    def __init__(self):
        self.var1 = "Instance of Class A"
        self.special = "Special"

class B(A):
    var1 = "Second Class"
    def __init__(self):

        self.var1 = "Instance of Class B"
        super().__init__()

a = A()
b = B()

print(b.var1, b.special)
