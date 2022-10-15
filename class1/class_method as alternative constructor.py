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
        # name =strc.split("-")
        # print(name)
        # return cls(name[0], name[1], name[2])
        return cls(*strc.split("-"))

akram = Employee("akram", 12345, "B.Tech")
khan = Employee("Khan", 6789, "M.Tech")
rahul = Employee.any("Rahul-1245-College Dropout")

print(rahul.study)

akram.change_leaves(10)
print(rahul.no_of_leaves)
print(akram.no_of_leaves)
print(rahul.no_of_leaves)
print(Employee.no_of_leaves)