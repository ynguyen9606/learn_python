class tamgiac:
    def __init__(self, canh_1, canh_2, canh_3):
        if canh_1 + canh_2 > canh_3 and canh_2 + canh_3 > canh_1 and canh_1 + canh_3 > canh_2:
            self.__canh_1 = canh_1
            self.__canh_2 = canh_2
            self.__canh_3 = canh_3
        else:
            raise ValueError("3 canh k phai la 1 tam giac ")
        
    def get_canh_1(self):
        return self.__canh_1
    
    def get_canh_2(self):
        return self.__canh_2
    
    def get_canh_3(self):
        return self.__canh_3

    def chuvi(self):
        return self.__canh_1 + self.__canh_2 +self.__canh_3
    
    def showInfo(self):
        print(f'tam giac gom 3 canh lan luot: {self.get_canh_1()}; {self.get_canh_2()}; {self.get_canh_3()} có chu vi la: {self.chuvi()}')


class tamgiacvuong(tamgiac):
    def __init__(self, canh_vuong_1, canh_dvuong_2):
        canh_huyen =(canh_vuong_1 ** 2 + canh_dvuong_2 ** 2) ** 0.5
        super().__init__(canh_vuong_1, canh_dvuong_2)

    def showInfo(self):
        print("tam giac vuong")
        super().showInfo()


class tamgiaccan(tamgiac):
    def __init__(self, canh_ben, canh_day, canh_huyen):
        super().__init__(canh_ben, canh_ben, canh_day)

    def showInfo(self):
        print("Tam giac can")
        super().showInfo()
    

class tamgiacdeu(tamgiaccan):
    def __init__(self, canh):
        super().__init__(canh, canh)

    def showInfo(self):
        print("Tam giac deu")
        super().showInfo()

def main():
    print("1. Tam giac thuong")
    print("2. Tam giac vuong")
    print("3. Tam giac can")
    print("4. Tam giac deu")

    try:
        choice = int(input("Nhap lua chon (1-4): "))

        if choice == 1:
            a = float(input("Nhap canh 1: "))
            b = float(input("Nhap canh 2: "))
            c = float(input("Nhap canh 3: "))
            tg = tamgiac(a, b, c)

        elif choice == 2:
            a = float(input("Nhap canh vuong thu 1: "))
            b = float(input("Nhap canh vuong thu 2: "))
            tg = tamgiacvuong(a, b)

        elif choice == 3:
            canh_ben = float(input("Nhap canh ben: "))
            canh_day = float(input("Nhap canh day: "))
            tg = tamgiaccan(canh_ben, canh_day)

        elif choice == 4:
            canh = float(input("Nhap canh: "))
            tg = tamgiacdeu(canh)

        else:
            print("Lua chon khong hop le!")
            return

        print("\n------")
        tg.showInfo()

    except ValueError as e:
        print("Loi:", e)

if __name__ == "__main__":
    main()
