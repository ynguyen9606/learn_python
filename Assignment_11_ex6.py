class Fraction:
    def __init__(self, Numerator, Denominator):
        self.__Numerator = Numerator
        self.__Denominator = Denominator
                
    def getter_Numerator(self):
        return self.__Numerator
    
    def getter_Denominator(self):
        return self.__Denominator
    
    def setter_Numerator(self, Numerator):
        self.__Numerator = Numerator
    
    def setter_Denominator(self, Denominator):
        if Denominator != 0:
            self.__Denominator = Denominator
        else:
            print("Mau so khong duoc bang 0 ")
    
    def inputInfo(self,):
        self.__Numerator = int(input("nhap tu so: "))
        while True:
            Denominator = int(input("Nhap mau so: "))
            if Denominator != 0:
                self.__Denominator = Denominator
                break
            else:
                print("Gia khong hop le, vui long nhap lai!")
            
    def viewInfo(self):
        print(f"phan so cua ban la: {self.__Numerator}/{self.__Denominator}")

    def reduce(self):
        num1 = abs(self.__Numerator)
        num2 = abs(self.__Denominator)

        while num2 != 0:
            num1, num2 = num2, num1 % num2
        
        greatest_common_divisor = num1
        self.__Numerator //= greatest_common_divisor
        self.__Denominator //= greatest_common_divisor

    def inverse_number(self):
        if self.__Numerator != 0:
            self.__Numerator, self.__Denominator = self.__Denominator, self.__Numerator
        else:
            print("Khong the lay nghich dao vi tu so bang 0")

    def add(self, other):
        new_numerator = self.__Numerator * other.__Denominator + self.__Denominator * other.__Numerator
        new_denominator = self.__Denominator * other.__Denominator
        result = Fraction(new_numerator, new_denominator)
        result.reduce()
        return result
    
    def sub(self, other):
        new_numerator = self.__Numerator * other.__Denominator - self.__Denominator * other.__Numerator
        new_denominator = self.__Denominator * other.__Denominator
        result = Fraction(new_numerator, new_denominator)
        result.reduce()
        return result
    
    def mul(self, other):
        new_numerator = self.__Numerator * other.__Numerator
        new_denominator = self.__Denominator * other.__Denominator
        result = Fraction(new_numerator, new_denominator)
        result.reduce()
        return result
    
    def div(self, other):
        if other.__Numerator == 0:
            print("Khong the chia cho phan so co tu so bang 0")
            return None

        new_numerator = self.__Numerator * other.__Denominator
        new_denominator = self.__Denominator * other.__Numerator
        result = Fraction(new_numerator, new_denominator)
        result.reduce()
        return result

class TestFraction:
    def main():
        print("Nhap phan so thu nhat:")
        ps1 = Fraction(0, 1)
        ps1.inputInfo()

        print("\nNhap phan so thu hai:")
        ps2 = Fraction(0, 1)
        ps2.inputInfo()

        print("\nPhan so thu nhat:")
        ps1.viewInfo()

        print("Phan so thu hai:")
        ps2.viewInfo()

        print("\nCong hai phan so:")
        ps1.add(ps2).viewInfo()

        print("Tru hai phan so:")
        ps1.sub(ps2).viewInfo()

        print("Nhan hai phan so:")
        ps1.mul(ps2).viewInfo()

        print("Chia hai phan so:")
        result = ps1.div(ps2)
        if result is not None:
            result.viewInfo()

TestFraction.main()
