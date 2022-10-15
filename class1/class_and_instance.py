class Employee:
    no_of_leaves = 8
    pass

akram = Employee()
rahul = Employee()

akram.name = "Akram"
rahul.name = "Rahul"
akram.no_of_leaves = 9
print(akram.__dict__)
print(Employee.__dict__)
print(Employee.no_of_leaves,akram.no_of_leaves,rahul.no_of_leaves)