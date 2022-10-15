class Employee:
    no_of_leaves = 8
    def __init__(self, s_name, s_roll, s_study):
        self.name = s_name
        self.roll = s_roll
        self.study = s_study
    def details(self):
        return f"Name is {self.name}\nRoll number = {self.roll}\nQ" \
               f"ualification = {self.study}"
    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves
    @classmethod
    def any(cls, strc):
        return cls(*strc.split("-"))
    @staticmethod
    def nameshow(name):
        return f"This is {name}"
class Student(Employee):
    def __init__(self, s_name, s_roll, s_study, s_mstatus):
        super().__init__(s_name, s_roll, s_study)
        self.name = s_name
        self.roll = s_roll
        self.study = s_study
        self.mstatus = s_mstatus

    def details_second(self):
        return f"Name is {self.name}\nRoll number = {self.roll}\nQ" \
               f"ualification = {self.study}\nMarital Status = {self.mstatus}"

akram = Employee("akram", 12345, "B.Tech")
khan = Employee("Khan", 6789, "M.Tech")
rahul = Employee.any("Rahul-1245-College Dropout")

monika = Student("Monika", 9696, "B.Sc","Unmarried")
priya = Student("Priya", 66666, "M.com","Married")

print(monika.no_of_leaves,"\n\n",priya.details())