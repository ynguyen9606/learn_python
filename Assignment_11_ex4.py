class SoNguyenTo:
    def __init__(self, x):
        if self.isSoNguyenTo(x):
            self.__a = x
        else:
            print(f"{x} khng phai la so nguyen to , k luu")
            self.__a = None

    def isSoNguyenTo(self, x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True
    
    def getA(self):
        return self.__a

    def setA(self, x):
        if self.isSoNguyenTo(x):
            self.__a = x
        else:
            print("khong set")
    
    def timSoNguyenToTiepTheo(self):
        n = self.__a + 1
        while True:
            if self.isSoNguyenTo(n):
                return n 
            n += 1

class Main:
    def main(self):
        s = SoNguyenTo(2)
        print(s.getA())
        s.setA(11)
        print(s.getA())

        s.__a = 100
        print(s.getA())
    
Main().main()