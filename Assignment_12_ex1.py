class dagiac:
    def __init__(self, so_canh):
        self.__so_canh = so_canh
        self.__canh = []

    def nhapcanh(self):
        self.__canh.clear()
        for i in range (self.__so_canh):
            x = float(input(f"nhap canh thu {i + 1}: "))
            self.__canh.append(x)
        
    def getsocanh(self):
        return self.__so_canh
    
    def getcanh(self):
        return self.__canh
    
    def chuvi(self):
        return sum(self.__canh)
    
class hinhbinhhanh(dagiac):
    def __init__(self, canh_day, canh_ben, chieu_cao):
        super().__init__(4)  # 4 ở đây là 4 cạnh (hình bình hành, chữ nhật, vuông)
        self.__canh_day = canh_day
        self.__canh_ben = canh_ben
        self.__chieu_cao = chieu_cao
        self._dagiac__canh = [canh_day, canh_ben, canh_day, canh_ben]
            # _ ở đây là phá đóng gói __canh
    def dientich(self):
        return self.__canh_day * self.__chieu_cao

class hinhchunhat(hinhbinhhanh):
    def __init__(self, dai, rong):
        self.__dai = dai
        self.__rong = rong
        super().__init__(dai, rong, rong) # khi thừa kế lớp hbh thì dai =day, rong1 = ben, rong2 = cao
    
    def dientich(self):
        return self.__dai * self.__rong

class hinhvuong(hinhchunhat):
    def __init__(self, canh):
        self.__canh = canh
        super().__init__(canh, canh) # tương tự như của hcn
    
def main():
    print("1. Hình bình hành")
    print("2. Hình chữ nhật")
    print("3. Hình vuông")

    chon = int(input("Chọn hình: "))

    if chon == 1:
        day = float(input("Nhập đáy: "))
        canh_ben = float(input("Nhập cạnh bên: "))
        chieu_cao = float(input("Nhập chiều cao: "))
        h = hinhbinhhanh(day, canh_ben, chieu_cao)

    elif chon == 2:
        dai = float(input("Nhập chiều dài: "))
        rong = float(input("Nhập chiều rộng: "))
        h = hinhchunhat(dai, rong)

    elif chon == 3:
        canh = float(input("Nhập cạnh: "))
        h = hinhvuong(canh)

    else:
        print("Lựa chọn không hợp lệ")
        return

    print("Chu vi:", h.chuvi())
    print("Diện tích:", h.dientich())


main()
