#thừa kế : tái sử dụng những thành phần đã có ở lớp khác , giúp dễ dàng mwor roongj
class Animal:
    def __init__(self, id, name, age):
        self.__id = id
        self.name = name
        self.age = age

    def get__id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id
    
    def move(self):
        print("run, walk, swim, jump, ...")
    
    def inputInfo(self):
        self.__id = int(input("input ID: "))
        self.name = input("input name: ")
        self.age = int(input("input age: "))

    def showInfo(self):
        print(f"""
              ID: {self.__id}
              name: {self.name}
              age: {self.age}
              """)
        
class Cat(Animal):
    def __init__(self, id, name, age, color):
        super().__init__(id, name, age)
        self.color = color
    
    def showInfoCat(self):
        super().showInfo()
        print(f"            color: {self.color}")

    def speak(self):
        print("meomeo")
    
    def moveCat(self):
        super().move()


cat1 = Cat(12, "Moon", 2, "black")
cat1.__id = 23 # do id nằm tỏng đogns gói nên k thao tác đc
cat1.set_id(55)# muốn thao tác cần dùng get, set
cat1.showInfo()
cat1.moveCat()
cat1.speak()

ani = Cat(56, "Pick", 3, "pink")
ani.showInfoCat()
ani.moveCat()
