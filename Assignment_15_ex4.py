import pickle
import os

class Student:
    def __init__(self, no, name, id, avgMark):
        self.no = no
        self.name = name
        self.id = id
        self.avgMark = avgMark

    def show(self):
        print(f'No: {self.no}')
        print(f'name: {self.name}')
        print(f'Id: {self.id}')
        print(f'Average Mark: {self.avgMark}')


class CRUD:
    def createStudent(self):
        students = []

        with open("Assignment_4_S8.txt", "rb") as file:
            try:
                while True:
                    students.append(pickle.load(file))
            except EOFError:
                pass

        if students:
            no = students[-1].no + 1
        else:
            no = 1
        
        print("STT tu dong:", no)

        name = input("Nhap ten (viet lien): ")
        id = input("Nhap ma sinh vien: ")
        avgMark = float(input("Nhap diem trung binh: "))

        student = Student(no, name, id, avgMark)

        with open("Assignment_4_S8.txt", "ab") as file:
            pickle.dump(student, file)

        print("Them sinh vien thanh cong!")
    
    def readStudent(self):
        try:
            with open("Assignment_4_S8.txt", "rb") as file:
                while True:
                    student = pickle.load(file)
                    student.show()
        except EOFError:
            pass
        except FileNotFoundError:
            print("File khong ton tai!")

    def updateStudent(self):
        students = []
        found = False

        id = input("Nhap id sinh vien can sua: ")
        newMark = float(input("Nhap diem trung binh moi: "))

        try:
            with open("Assignment_4_S8.txt", "rb") as file:
                while True:
                    students.append(pickle.load(file))
        except EOFError:
            pass
        except FileNotFoundError:
            print("File khong ton tai!")
            return

        for st in students:
            if st.id == id:
                st.avgMark = newMark
                found = True
                break

        if not found:
            print(f"Khong tim thay sinh vien co id = {id}")
            return

        with open("Assignment_4_S8.txt", "wb") as file:
            for st in students:
                pickle.dump(st, file)

        print("Cap nhat diem thanh cong!")
    
    def deleteStudent(self):
        students = []
        found = False
        id = input("Nhap id sinh vien can xoa: ")

        try:
            with open("Assignment_4_S8.txt", "rb") as file:
                while True:
                    students.append(pickle.load(file))
        except EOFError:
            pass

        new_list = []

        for st in students:
            if st.id == id:
                found = True
            else:
                new_list.append(st)

        if not found:
            print(f"Khong tim thay sinh vien co id = {id}")
            return

        with open("Assignment_4_S8.txt", "wb") as file:
            for st in new_list:
                pickle.dump(st, file)

        print("Da xoa sinh vien!")
    
    def searchStudent(self):
        students = []

        avgLow = float(input("Nhap diem thap nhat: "))
        avgHigh = float(input("Nhap diem cao nhat: "))

        try:
            with open("Assignment_4_S8.txt", "rb") as file:
                while True:
                    students.append(pickle.load(file))
        except EOFError:
            pass

        print("Danh sach sinh vien tim duoc:")

        for st in students:
            if avgLow <= st.avgMark <= avgHigh:
                st.show()

    def sortStudent(self):
        students = []

        try:
            with open("Assignment_4_S8.txt", "rb") as file:
                while True:
                    students.append(pickle.load(file))
        except EOFError:
            pass

        students.sort(key=lambda x: x.avgMark, reverse=True)

        print("Danh sach sau khi sap xep:")

        for st in students:
            st.show()

default_students = [
    Student(1, "NguyenVanAn", "ck16001", 8.1),
    Student(2, "LuongVanKhoan", "ck16002", 8.2),
    Student(3, "TruongThanhNhan", "ck16003", 7.5),
    Student(4, "NguyenVanLong", "ck16004", 7.0),
    Student(5, "TruongTienLoi", "ck16005", 6.4),
    Student(6, "HoangVanPhuc", "ck16006", 7.9),
    Student(7, "TruongMinhDuc", "ck16007", 8.9),
    Student(8, "LuongCongToan", "ck16008", 9.1),
    Student(9, "TranQuangHung", "ck16009", 8.4),
    Student(10, "NguyenThanhTam", "ck16010", 8.5)
]

if not os.path.exists("Assignment_4_S8.txt"):
    with open("Assignment_4_S8.txt", "wb") as file:
        for st in default_students:
            pickle.dump(st, file)

crud = CRUD()

while True:
    print("\n===== STUDENT MANAGEMENT =====")
    print("1. Create Student")
    print("2. Read Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Sort Student")
    print("7. Exit")

    choice = input("Chon chuc nang: ")

    if choice == "1":
        crud.createStudent()

    elif choice == "2":
        crud.readStudent()

    elif choice == "3":
        crud.updateStudent()

    elif choice == "4":
        crud.deleteStudent()

    elif choice == "5":
        crud.searchStudent()

    elif choice == "6":
        crud.sortStudent()

    elif choice == "7":
        print("Thoat chuong trinh")
        break

    else:
        print("Lua chon khong hop le!")