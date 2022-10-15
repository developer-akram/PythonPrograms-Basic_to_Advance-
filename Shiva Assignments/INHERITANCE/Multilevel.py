class Input:
    def accept(self,a,b):
        self.a = a
        self.b = b
        print(f"Input A = {self.a},\tInput B = {self.b}")
class Area(Input):
    def tarea(self):
        self.x = "triangle"
        self.area = (self.a * self.b) / 2
    def rarea(self):
        self.x = "rectangle"
        self.area = self.a * self.b
class ShowArea(Area):
    def displayarea(self):
        print(f"Area of {self.x} = {self.area}")

tri = ShowArea()
tri.accept(10,16)
tri.tarea()
tri.displayarea()

rec = ShowArea()
rec.accept(6,20)
rec.rarea()
rec.displayarea()



