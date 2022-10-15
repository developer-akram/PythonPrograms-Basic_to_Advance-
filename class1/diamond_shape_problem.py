class A:
    def printdetails(self):
        print("This is From class A")

class B(A):
    def printdetails(self):
        print("This is From class B")
        pass

class C(A):
    def printdetails(self):
        print("This is From class C")
        pass

class D(C, B):
    def printdetails(self):
        print("This is From class D")
        pass

a = A()
b = B()
c = C()
d = D()

d.printdetails()