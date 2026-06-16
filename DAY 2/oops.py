# # using constructors 

# class Student:
#     def __init__(self, name, marks, email):
#         self.name = name
#         self.marks = marks
#         self.email = email

# s1 = Student("Karan", 99, "karan2005@gmail.com")
# print(s1.name, s1.marks, s1.email)

# s2 = Student("Arjun", 87, "arjun323@gmail.com")
# print(s2.name, s2.marks, s2.email)

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def Welcome(self):
        print("Welcome Student,", self.name)

    def get_marks(self):
        return self.marks

s1 = Student("Rohit", 87)
s1.Welcome()
print(s1.get_marks())