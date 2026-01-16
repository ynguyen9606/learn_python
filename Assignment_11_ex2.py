class NhanVien():
    def __init__(self, ma_nhan_vien = "", ten = "", tuoi = 0, dia_chi = "", luong = 0,  gio_lam = 0):
        self.__ma_nhan_vien = ma_nhan_vien
        self.ten = ten
        self.tuoi = tuoi
        self.dia_chi = dia_chi
        self.luong = luong
        self.gio_lam = gio_lam
    
    def get_luong(self):
        return self.luong
    
    def get_gio_lam(self):
        return self.gio_lam
    
    def inputInfo(self):
        self.__ma_nhan_vien = (input("Nhap ma nhan vien : "))
        self.ten = input("Nhap ho va ten nhan vien : ") 
        self.tuoi = int(input("Nhap tuoi : "))
        self.dia_chi = input("Nhap dia chi nhan vien : ")
        self.luong = float(input("Nhap luong : "))
        self.gio_lam = float(input("Nhap so gio lam : "))

    def printInfo(self):
        print(f"MSNV: {self.__ma_nhan_vien}")
        print(f"Ho va ten: {self.ten}")
        print(f"Tuoi: {self.tuoi}")
        print(f"Dia chi: {self.dia_chi}")
        print(f"Luong: {self.luong}")
        print(f"Gio lam: {self.gio_lam}")

    def tinhThuong(self):
        if self.get_gio_lam() >= 200:
            return self.get_luong() * 0.2
        elif self.get_gio_lam() < 200 and self.get_gio_lam() >= 100:
            return self.get_luong() * 0.1
        else:
            return 0
        
class Main():
    def main():
        NV = NhanVien()
        NV.inputInfo()
        NV.printInfo()

        print(f"thuong cua nhan vien la: {NV.tinhThuong()}")

Main.main()