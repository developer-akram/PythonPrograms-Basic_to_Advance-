class Rarea:
    def rarea(self):
        self.x = "rectangle"
        self.area = self.a * self.b
class Tarea:
    def tarea(self):
        self.x = "triangle"
        self.area = (self.a * self.b) / 2
class ShowArea(Tarea, Rarea):
    def accept(self,a,b):
        self.a = a
        self.b = b
        print(f"Input A = {self.a},\tInput B = {self.b}")
    def __str__(self):
        return f"Area of {self.x} = {self.area}"

tri = ShowArea()
tri.accept(6,9)
tri.tarea()
print(tri)

rec = ShowArea()
rec.accept(4,9)
rec.rarea()
print(rec)
