class Student:
    def __init__(self, id = "", diem_trung_binh = 0, tuoi = 0, lop = 0):
        self.__id = id
        self.diem_trung_binh = diem_trung_binh
        self.tuoi = tuoi
        self.lop = lop

    def inputInfo(self):
        while True:
            self.__id  = input("Nhap ID gom 8 ky tu: ")
            if len(self.__id) == 8:
                break
            print("phai 8 ky tu")

        while True:
            self.diem_trung_binh = float(input("Nhập điểm trung bình: "))
            if 0.0 <= self.diem_trung_binh <= 10.0:
                break
            print("Điểm phải từ 0.0 đến 10.0!")

        while True:
            self.tuoi = int(input("Nhập tuổi: "))
            if self.tuoi >= 18:
                break
            print("Tuổi phải >= 18!")

        while True:
            self.lop = input("Nhập lớp: ")
            if self.lop.startswith("A") or self.lop.startswith("C"):
                break
            print("Lớp phải bắt đầu bằng A hoặc C!")

    def showInfo(self):
        print("ID:", self.__id)
        print("Điểm trung bình:", self.diem_trung_binh)
        print("Tuổi:", self.tuoi)
        print("Lớp:", self.lop)

    def hocBong(self):
        return self.diem_trung_binh > 8.0
    
class Main():
    def main(self):
        sv = Student()
        sv.inputInfo()
        sv.showInfo()

        if sv.hocBong():
            print("Sinh viên được học bổng")
        else:
            print("Sinh viên không được học bổng")

Main().main()