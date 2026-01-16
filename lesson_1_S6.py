class Cat:
    def __init__(self, name, age, color, gender): # tên, tuổi, màu, giới tính -> dùng biến(thuộc tính-attribute)
        self.name = name
        self.age = age
        self.color = color
        self.gender = gender

    def move(self):#di chuyển, tiếng kêu,..-> dùng hàm (hành vi (phương thức) -method)
        print("Run, wald")

    def speak(self):
        print("meo meo")
    
    def InputInfo(self):
        self.name = input("Input name: ")
        self.age = input("Input age: ")
        self.color = input("Input color: ")
        self.gender = input("Input gender: ")
    
    def ShowInfo(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Color: {self.color}")
        print(f"Gender: {self.gender}")

    
cat1 = Cat("Moon",2, "black", "Male")
#nếu muốn sửa
print(cat1.name)
cat1.InputInfo()
cat1.ShowInfo()