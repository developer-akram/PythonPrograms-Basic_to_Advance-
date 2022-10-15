class Name:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
        # self.email = f"{self.f_name}.{self.l_name}@khanstar.com"
    def showname(self):
        return f"First name is {self.f_name}\nSurname is {self.l_name}\n\n{self.f_name} {self.l_name}"
    @property
    def email(self):
        if self.l_name == None or self.l_name == None:
            return "Email is not set yet,Please set it using settter"
        return f"{self.f_name}.{self.l_name}@khanstar.com"
    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.f_name = names.split(".")[0]
        self.l_name = names.split(".")[1]
    @email.deleter
    def email(self):
        self.f_name = None
        self.l_name = None

name1 = Name("Akram","Khan")
print(name1.email)

name1.f_name = "Bikram"
print(name1.email)

name1.email = "Firstpiece.Secondpiece@khanstar.com"
print(name1.f_name)
del name1.email
print(name1.email)
name1.email = "First.Second@khanstar.com"
print(name1.email)