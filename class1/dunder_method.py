class Employee:
    no_of_leaves = 8
    def __init__(self, s_name, s_roll, s_study):
        self.name = s_name
        self.roll = s_roll
        self.study = s_study
    def __add__(self, other):
        return self.roll + other.roll
    def __truediv__(self, other):
        return self.roll / other.roll
    def __repr__(self):
        return f"Employee ('{self.name}', {self.roll}, '{self.study}')"
    # def __str__(self):
    #     return f"Str Name is {self.name}\nStrRoll number = {self.roll}\nStr Q" \
    #            f"ualification = {self.study}"
    def details(self):
        return f"Name is {self.name}\nRoll number = {self.roll}\nQ" \
               f"ualification = {self.study}"

akram = Employee("Akram", 66, "B.Tech")
khan = Employee("Khan", 22, "M.Tech")

print(str(akram))
# print(akram)