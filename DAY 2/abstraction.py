# # ABSTRACTION 

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.br = False
#         self.cluth = False
    
#     def start(self):
#         self.cluth = True
#         self.acc = True
#         print("Car Started....")
    
# car1 = Car()
# car1.start()

class BankAccount:
    def __init__(self):
        self.__balance = 0 
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def get_balance(self):
        return self.__balance
    
account = BankAccount()
account.deposit(1000)

print(account.get_balance())