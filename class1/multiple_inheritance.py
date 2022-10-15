class Employee:
    no_of_leaves = 8
    var = 1
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

class Player :
    var = 11
    def __init__(self, s_name, s_play ):
        self.name = s_name
        self.play = s_play

    def player_details(self):
        return f"Name is {self.name}\nPlay {self.play}"

class Final_list(Employee, Player):
    var =111
    language = "C++"
    def show_language(self):
        return self.language

akram = Employee("akram", 12345, "B.Tech")
khan = Employee("Khan", 6789, "M.Tech")
rahul = Employee.any("Rahul-1245-College Dropout")

pintu = Player("Pintu", ["Cricket", "Football" , "Tennis"])
mintu = Player("Mintu", ["Volleyball"])
akash = Final_list("Akash", 124578 , "Madhyamik Pass")
print(akash.show_language())