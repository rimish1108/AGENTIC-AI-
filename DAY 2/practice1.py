# Create a Student class that takes name and marks of 3 subjects as arguments in constructors. Then create a method to print the average.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("Hello")
    
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hii", self.name, "Your average score is :", sum/3)
s1 = Student("Kartik",[99, 98, 95])
print(s1.name, s1.marks)
s1.get_avg()
s1.hello()