# class Car:
#     def __init__(self, type):
#         self.type = type
    
#     @staticmethod
#     def start():
#         print("Car started...")
    
#     @staticmethod
#     def stop():
#         print("Car Stopped...")

# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         self.name = name
#         super().__init__(type)

# car1 = ToyotaCar("Prius", "Electric")
# print(car1.type)


class Person:
    name = "anonymous"
    
    # def ChangeName(self, name):
    #     self.__class__.name = name
    
    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Rishab")
# print(p1.name)
print(Person.name)
