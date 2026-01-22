#đóng gói (encapsulate): ẩn dấu , che dấu thuộc tính , phương thức,
#nghĩa là k cung cấp công khai các thành phần này ra ngoài lớp
# Cách thức : dùng __ đặt trc tên của thuộc tính hay phương thức
class Student:
    def __init__(self, id, name, age):
        self.__id = id
        self.name = name
        self.age = age

    def __ShowInfo__(self):
        print(self.__id)

    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id

St1 = Student(1234, "Alex", 18)
print(St1.name)
St1.__ShowInfo__()

St1.set_id(5678)# dùng phương thức gián tiếp bằng set và get
print(St1.get_id())

print(St1.__id)# sẽ bị ẩn id(đóng gói id),nếu muốn mở đóng gói này thì thêm __ sau nó
