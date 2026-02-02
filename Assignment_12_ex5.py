class Animal:
    def __init__(self, ten, tuoi, mota):
        self.__ten = ten
        self.__tuoi = tuoi
        self.__mota = mota

    def getTen(self):
        return self.__ten

    def xemThongTin(self):
        print(f"loai: {self.__class__.__name__}")
        print(f"ten: {self.__ten}")
        print(f"tuoi: {self.__tuoi}")
        print(f"mo ta: {self.__mota}")

    def tiengKeu(self):
        print("dong vat phat ra tieng keu")


class Tiger(Animal):
    def tiengKeu(self):
        print("Ho gam: GAOOOO")


class Dog(Animal):
    def tiengKeu(self):
        print("Cho sua: GAU GAU")


class Cat(Animal):
    def tiengKeu(self):
        print("Meo keu: MEO MEO")


class Chuong:
    def __init__(self, machuong):
        self.machuong = machuong
        self.AnimalList = []

    def themConVat(self, animal):
        self.AnimalList.append(animal)

    def xoaConVat(self, ten):
        for a in self.AnimalList:
            if a.getTen() == ten:
                self.AnimalList.remove(a)
                print("da xoa dong vat co ten:", ten)
                return
        print("khong tim thay con vat muon xoa!")


class Zoo:
    def __init__(self):
        self.DanhSachChuong = []

    def themChuong(self, chuong):
        self.DanhSachChuong.append(chuong)

    def xoaChuong(self, machuong):
        for c in self.DanhSachChuong:
            if c.machuong == machuong:
                self.DanhSachChuong.remove(c)
                print("da xoa chuong:", machuong)
                return
        print("khong tim thay chuong muon xoa!")


class TestZoo:
    @staticmethod
    def main():
        zoo = Zoo()

        while True:
            print("\n---------------")
            print("1. Them chuong")
            print("2. Xoa chuong")
            print("3. Them con vat")
            print("4. Xoa con vat")
            print("5. Xem tat ca cac con vat")
            print("6. Thoat")

            chon = input("Chon chuc nang: ")

            if chon == "1":
                ma = input("Nhap ma chuong: ")
                zoo.themChuong(Chuong(ma))
                print("Da them chuong!")

            elif chon == "2":
                ma = input("Nhap ma chuong can xoa: ")
                zoo.xoaChuong(ma)

            elif chon == "3":
                ma = input("Nhap ma chuong: ")
                for c in zoo.DanhSachChuong:
                    if c.machuong == ma:

                        while True:
                            loai = input("Nhap loai (Tiger/Dog/Cat): ")

                            if loai in ["Tiger", "Dog", "Cat"]:
                                ten = input("Nhap ten con vat: ")

                                while True:
                                    try:
                                        tuoi = int(input("Nhap tuoi: "))
                                        break
                                    except:
                                        print("Tuoi phai la so! Nhap lai!")

                                mota = input("Nhap mo ta: ")

                                if loai == "Tiger":
                                    c.themConVat(Tiger(ten, tuoi, mota))
                                elif loai == "Dog":
                                    c.themConVat(Dog(ten, tuoi, mota))
                                elif loai == "Cat":
                                    c.themConVat(Cat(ten, tuoi, mota))

                                print("Da them con vat!")
                                break
                            else:
                                print("Loai khong hop le! Vui long nhap lai!")

                        break
                else:
                    print("Khong tim thay chuong!")

            elif chon == "4":
                ma = input("Nhap ma chuong: ")
                ten = input("Nhap ten con vat can xoa: ")
                for c in zoo.DanhSachChuong:
                    if c.machuong == ma:
                        c.xoaConVat(ten)
                        break
                else:
                    print("Khong tim thay chuong!")

            elif chon == "5":
                for c in zoo.DanhSachChuong:
                    print(f"\n--- Chuong {c.machuong} ---")
                    for a in c.AnimalList:
                        a.xemThongTin()
                        a.tiengKeu()
                        print("------------------")

            elif chon == "6":
                print("Thoat chuong trinh!")
                break

            else:
                print("Lua chon khong hop le!")


TestZoo.main()
