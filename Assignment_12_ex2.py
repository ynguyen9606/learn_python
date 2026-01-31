import math

class Diem:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def show(self):
        print(f"Tâm: ({self.__x}, {self.__y})")


class Elip(Diem):
    def __init__(self, x, y, a, b):
        super().__init__(x, y)
        self.setA(a)
        self.setB(b)

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def setA(self, a):
        if a > 0:
            self.__a = a
        else:
            raise ValueError("Bán trục a phải > 0")

    def setB(self, b):
        if b > 0:
            self.__b = b
        else:
            raise ValueError("Bán trục b phải > 0")

    def dienTich(self):
        return math.pi * self.__a * self.__b

    def show(self):
        super().show()
        print(f"Bán trục lớn a = {self.__a}")
        print(f"Bán trục nhỏ b = {self.__b}")
        print(f"Diện tích elip = {self.dienTich():.2f}")


class DuongTron(Elip):
    def __init__(self, x, y, r):
        self.setR(r)
        super().__init__(x, y, r, r)

    def getR(self):
        return self.__r

    def setR(self, r):
        if r > 0:
            self.__r = r
        else:
            raise ValueError("Bán kính phải > 0")

    def dienTich(self):
        return math.pi * self.__r ** 2

    def show(self):
        super().show()
        print(f"(Đường tròn, bán kính r = {self.__r})")

def main():
    try:
        x = float(input("Nhập tọa độ x: "))
        y = float(input("Nhập tọa độ y: "))
        a = float(input("Nhập bán trục lớn a: "))
        b = float(input("Nhập bán trục nhỏ b: "))

        elip = Elip(x, y, a, b)
        elip.show()

        r = float(input("Nhập bán kính r: "))
        tron = DuongTron(x, y, r)
        tron.show()

    except ValueError as e:
        print("Lỗi:", e)

if __name__ == "__main__":
    main()