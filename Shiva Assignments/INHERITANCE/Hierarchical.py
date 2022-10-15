class Tarea:
    def accept(self,a,b):
        self.a = a
        self.b = b
        print(f"Input A = {self.a},\tInput B = {self.b}")
    def tarea(self):
        self.x = "triangle"
        self.area = (self.a * self.b) / 2
    def __str__(self):
        return f"Area of {self.x} = {self.area}"
class Rarea(Tarea):
    def rarea(self):
        self.x = "rectangle"
        self.area = self.a * self.b
class Carea(Tarea):
    def carea(self):
        self.x = "circle"
        self.area = self.a * (self.b) ** 2

tri = Tarea()
tri.accept(10,5)
tri.tarea()
print(tri)

rec = Rarea()
rec.accept(10, 20)
rec.rarea()
print(rec)

cir = Carea()
cir.accept(3.14,5)
cir.carea()
print(cir)