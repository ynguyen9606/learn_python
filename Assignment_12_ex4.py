class Person:
    def __init__(self, name, sex, date_birth, address):
        self.__name  = name
        self.__sex = sex
        self.__date_birth = date_birth
        self.__address = address

    def get_name(self):
        return self.__name
    
    def get_sex(self):
        return self.__sex
    
    
    def get_date_birth(self):
        return self.__date_birth
    
    def get_address(self):
        return self.__address
    
    def inputInfo(self):
        self.__name = input("nhap ten nhan su: ")
        self.__sex = input("nhap gioi tinh: ")
        self.__date_birth = input("nhap ngay sinh: ")
        self.__address = input("nhap dia chi: ")

    def showInfo(self):
        print("\nthong tin nhan su gom: ")
        print(f"ten: {self.get_name()}")
        print(f"gioi tinh: {self.get_sex()}")
        print(f"ngay sinh: {self.get_date_birth()}")
        print(f"dia chi: {self.get_address()}")
    

class Student(Person):
    def __init__(self, name="", sex="", date_birth="", address="",
             ID="", average_score=0.0, email=""):
        self.__ID = ID
        self.__average_score = average_score
        self.__email = email 
        super().__init__(name, sex, date_birth, address)

    def inputInfo(self):
        super().inputInfo()

        while True:
            self.__ID = input("nhap ma sinh vien (8 ky tu): ")
            if len(self.__ID) == 8:
                break
            print("ma sinh vien khong dung yeu cau !")

        while True:
            self.__average_score = float(input("nhap diem trung binh cua sinh vien: "))
            if 0.0 <= self.__average_score <= 10.0:
                break
            print("diem trung binh khong hop le !")

        while True:
            self.__email = input("nhap email: ")
            if "@" in self.__email and " " not in self.__email:
                break
            print("email khong hop le !")
        
    def showInfo(self):
        super().showInfo()
        print(f"ma sinh vien la: {self.__ID}")
        print(f"diem trung binh cua sinh vien la: {self.__average_score}")
        print(f"email sinh vien la: {self.__email}")

    def Check_scholarships(self):
        return self.__average_score >= 8


class  StudentTest:
    def __init__(self):
        self.students = []
    
    def inputStudents(self):
        n = int(input("nhap so sinh vien: "))
        for i in range(n):
            print(f"\nsinh vien {i+1}")
            stu = Student()
            stu.inputInfo()
            self.students.append(stu)

    def showall(self):
        for stu in self.students:
            stu.showInfo()
    
    def showmax_min(self):
        max_stu = max(self.students, key=lambda x: x._Student__average_score)
        min_stu = min(self.students, key=lambda x: x._Student__average_score)

        print("\nsinh vien cao diem nhat")
        max_stu.showInfo()

        print("\nSinh viên điểm thấp nhất:")
        min_stu.showInfo()
    
    def shearchID(self):
        find = input("nhap ma sinh vien can tim: ")
        for stu in self.students:
            if stu._Student__ID == find:
                stu.showInfo()
                return
        print(f"khong co sinh vien nao co ma la: {find}")

    def sortName(self):
        self.students.sort(key = lambda x: x.get_name())
        self.showall()
    
    def showScholarship(self):
        list_stu = [stu for stu in self.students if stu.Check_scholarships()]
        list_stu.sort(key=lambda x: x._Student__average_score, reverse=True)

        for sv in list_stu:
            print("----------------")
            sv.showInfo()

    def menu(self):
        while True:
            print("----------------")
            print("1. nhap n sinh vien")
            print("2. hien thi tat ca thong tin sinh vien")
            print("3. sinh vien co diem cao nhat va thap nhat")
            print("4. tim sinh vien theo ma sinh vien ")
            print("5. sap xep sinh vien theo A-Z")
            print("6. sinh vien duoc hoc bong")
            print("7. thoat")

            choice = input("nhap lua chon: ")

            if choice == "1":
                self.inputStudents()
            elif choice == "2":
                self.showall()
            elif choice == "3":
                self.showmax_min()
            elif choice == "4":
                self.shearchID()
            elif choice == "5":
                self.sortName()
            elif choice == "6":
                self.showScholarship()
            elif choice == "7":
                print("thoat!")
                break
            else:
                print("lua chon k hop le!")
test = StudentTest()
test.menu()

class Teacher(Person):
    def __init__(self, name="", sex="", date_birth="", address="",
                 class_name="", wage=0.0, time_month=0):
        self.__class_name = class_name
        self.__wage = wage
        self.__time_month = time_month
        super().__init__(name, sex, date_birth, address)

    def inputInfo(self):
        super().inputInfo()

        while True:
            self.__class_name = input("nhap ten lop day: ").upper()
            if self.__class_name and self.__class_name[0].upper() in ["G", "H", "I", "K", "L", "M"]:
                break
            print("ten lop day khong hop le!")

        while True:
            try:
                self.__wage = float(input("nhap luong mot gio day: "))
                if self.__wage > 0:
                    break
                print("luong phai lon hon 0!")
            except ValueError:
                print("vui long nhap so!")
            
        while True:
            try:
                self.__time_month = int(input("nhap so gio day trong thang: "))
                if self.__time_month >= 0:
                    break
                print("so gio khong duoc am!")
            except ValueError:
                print("vui long nhap so nguyen!")
    
    def Salary(self):
        salary = self.__wage * self.__time_month

        if self.__class_name[0] in ["L", "M"]:
            salary += 200000

        return salary

    def showInfo(self):
        super().showInfo()

        print(f"lop day: {self.__class_name}")
        print(f"luong 1 gio day: {self.__wage}")
        print(f"so gio day trong thang: {self.__time_month}")
        print(f"luong thuc nhan: {self.Salary()}")


class TeacherTest:
    def __init__(self):
        self.teachers = []

    def inputTeachers(self):
        while True:
            try:
                n = int(input("nhap so giang vien: "))
                if n > 0:
                    break
                print("so luong phai > 0!")
            except ValueError:
                print("vui long nhap so nguyen!")

        for i in range(n):
            print(f"\nGiang vien {i+1}")
            gv = Teacher()
            gv.inputInfo()
            self.teachers.append(gv)

    def showAll(self):
        if not self.teachers:
            print("chua co giang vien nao!")
            return

        for gv in self.teachers:
            print("----------------")
            gv.showInfo()

    def showMaxSalary(self):
        if not self.teachers:
            print("chua co giang vien nao!")
            return

        max_teacher = max(self.teachers, key=lambda x: x.Salary())
        print("\nGiang vien co luong cao nhat:")
        max_teacher.showInfo()

    def menu(self):
        while True:
            print("----------------")
            print("1. nhap n giang vien")
            print("2. hien thi tat ca giang vien")
            print("3. hien thi giang vien co luong cao nhat")
            print("4. thoat")

            choice = input("nhap lua chon: ")

            if choice == "1":
                self.inputTeachers()
            elif choice == "2":
                self.showAll()
            elif choice == "3":
                self.showMaxSalary()
            elif choice == "4":
                print("thoat chuong trinh!")
                break
            else:
                print("lua chon khong hop le!")


test = TeacherTest()
test.menu()