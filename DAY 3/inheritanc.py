# class Student:
#     def __init__(self, name):
#         self.name = name
# s1 = Student("Raksha")
# print(s1.name)
# del s1 # delete the object 
# print(s1)


class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
    
    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345", "zgdx")
print(acc1.acc_no)
print(acc1.reset_pass())

