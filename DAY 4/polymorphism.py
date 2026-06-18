# print(1 + 2) # 3 
# print(type(1))
# print("Kartik"+ "Sharma")  # concatenate
# print(type("Kartik"))
# print([1, 2, 3] + [4, 5, 6])  # merge
# print(type([1, 2, 3]))



class Complex:
    def __init__(self, real, img): # img -> imaginary numbers 
        self.real = real
        self.img = img

    def showNumbers(self):
        print(self.real, "i + ", self.img,"j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)
    

num1 = Complex(1, 3)
num1.showNumbers()

num2 = Complex(4, 6)
num2.showNumbers()

num4 = num1 - num2
num4.showNumbers()

