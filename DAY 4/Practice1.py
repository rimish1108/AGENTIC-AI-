class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    
    def showDetails(self):
        print("Role = ", self.role)
        print("Department = ", self.dept)
        print("Salary = ", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", 95000)
    
    def Details(self):
        print("Name = ", self.name)
        print("Age = ", self.age)


engg1 = Engineer("Elon Musk", 40)
engg1.Details()
engg1.showDetails()