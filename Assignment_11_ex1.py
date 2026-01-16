class SoHoc():
    def __init__(self, number1 = 0, number2 = 0):
        self.__number1 = number1
        self.__number2 = number2

    def get_number1(self):
        return self.__number1
    
    def get_number2(self):
        return self.__number2
    
    def set_number1(self, number1):
        self.__number1 = number1
    
    def set_number2(self, number2):
        self.__number2 = number2

    def inputInfo(self):
        self.__number1 = float(input("nhap so thu nhat num1 = "))
        self.__number2 = float(input("nhap so thu hai num2 = "))

    def printInfo(self):
        print(f"Num1 = {self.__number1}")
        print(f"Num2 = {self.__number2}")

    def addition(self):
        return self.get_number1() + self.get_number2()
    
    def subtract(self):
        if self.get_number1() >= self.get_number2():
            return self.get_number1() - self.get_number2()
        else:
            return self.get_number2() - self.get_number1()
        
    def multi(self):
        return self.get_number1() * self.get_number2()
    
    def division(self):
        if self.get_number2() != 0:
            return self.get_number1() / self.get_number2()
        else:
            return "calculation error"

class Main:
    def main():
        sh = SoHoc()
        sh.inputInfo()
        sh.printInfo()

        print("addition =", sh.addition())
        print("subtract =", sh.subtract())
        print("multi =", sh.multi())
        print("division =", sh.division())

Main.main()