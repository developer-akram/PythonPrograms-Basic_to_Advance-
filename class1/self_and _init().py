class Employee:
    def __init__(self, s_name, s_roll, s_study):
        self.name = s_name
        self.roll = s_roll
        self.study = s_study
    def details(self):
        return f"Name is {self.name}\nRoll number = {self.roll}\nQualification = {self.study}"

akram = Employee("akram", 12345, "B.Tech")
khan = Employee("Khan", 6789, "M.Tech")
# akram.name = "Akram"
# khan.name = "Khan"
# akram.roll = 12345
# khan.roll = 6789
# akram.study = "B.Tech"
# khan.study = "M.tech"
print(akram.details()+"\n"+khan.details())